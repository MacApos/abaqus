from abaqus import *
from abaqusConstants import *

def Macro2(radius, length, thickness, part, model):
    # Abaqus creates a Model object named Model-1 when a session is started.
    # A ConstrainedSketch object contains the entities that are used to create a sketch.
    my_model = mdb.Model(name=model, modelType=STANDARD_EXPLICIT)
    s = mdb.models[model].ConstrainedSketch(name='__profile__',
        sheetSize=200.0)
    g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints

    # This method makes the ConstrainedSketch object the primary object in the current viewport.
    # The sketch remains the primary object in the current viewport until an unsetPrimaryobject command is issued.

    # STANDALONE: Indicates a new stand-alone sketch. The current viewport is cleared and is replaced by the stand-alone
    # sketch. The view direction is set to –.
    s.setPrimaryObject(option=STANDALONE)
    s.CircleByCenterPerimeter(center=(0.0, 0.0), point1=(radius, 0.0))
    s.CircleByCenterPerimeter(center=(0.0, 0.0), point1=(radius-thickness, 0.0))

    # # This method creates a Part object and places it in the parts repository.
    p = mdb.models[model].Part(name=part, dimensionality=THREE_D,
        type=DEFORMABLE_BODY)
    p = mdb.models[model].parts[part]
    p.BaseSolidExtrude(sketch=s, depth=length)
    s.unsetPrimaryObject()
    p = mdb.models[model].parts[part]
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    del mdb.models[model].sketches['__profile__']

my_string = "elon"
my_radius = 100
my_length = 100
my_thickness =50
my_part = "Cylinder"

Macro2(my_radius, my_length, my_thickness, my_part, my_string)