from abaqus import *
from abaqusConstants import *
import regionToolset

if mdb.models.keys()[0] != "Cantilever Beam":
    mdb.models.changeKey(fromName=mdb.models.keys()[0], toName="Cantilever Beam")

cantileverModel = mdb.models["Cantilever Beam"]

import part

cantileverSketch = cantileverModel.ConstrainedSketch(name="Beam Section", sheetSize=5)
cantileverSketch.rectangle(point1=(0.0, 0.0), point2=(25.0, 20.0))

cantileverPart = cantileverModel.Part(name="Beam", dimensionality=THREE_D, type=DEFORMABLE_BODY)
cantileverPart.BaseSolidExtrude(sketch=cantileverSketch, depth=200.0)

import material
cantileverMaterial = cantileverModel.Material(name="Steel")
cantileverMaterial.Density(table=((7800, ), ))
cantileverMaterial.Elastic(table=((200E9, 0.3), ))

import section
cantileverSection = cantileverModel.HomogeneousSolidSection(name="Cantilever Section", material="Steel")

region_of_cantilever = (cantileverPart.cells, )
cantileverPart.SectionAssignment(region=region_of_cantilever, sectionName="Cantilever Section")

import assembly
cantileverAssembly = cantileverModel.rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=cantileverAssembly)
cantileverInstance = cantileverAssembly.Instance(name="Cantilever Instance", part=cantileverPart)

"""Static step is used to simulate load"""
cantileverModel.StaticStep(name="Apply load", previous="Initial", description="Load is applied during this step")

if cantileverModel.fieldOutputRequests.keys()[0] != "Required Filed Output":
   cantileverModel.fieldOutputRequests.changeKey(fromName=cantileverModel.fieldOutputRequests.keys()[0],
                                                 toName="Required Field Output")

cantileverModel.fieldOutputRequests["Required Field Output"].setValues(variables=("S", "E", "PEMAG", "U", "RF", "CF"))

"""Apply pressure loads"""
top_face_x = 12.5
top_face_y = 20.0
top_face_z = 100.0


def find_face(x, y, z):
    coordinates = (x, y, z)
    face = cantileverInstance.faces.findAt((coordinates, ))
    face_region = regionToolset.Region(side1Faces=face)
    return face_region


cantileverModel.Pressure(name="Uniform Pressure", createStepName="Apply load",
                         region=find_face(12.5, 20.0, 100.0), distributionType=UNIFORM,
                         magnitude=0.5, amplitude=UNSET)

coordinates = (12.5, 10.0, 0.0)
face = cantileverInstance.faces.findAt((coordinates,))
face_region = regionToolset.Region(side1Faces=face)

cantileverModel.EncastreBC(name='One end fixed', createStepName='Initial', region=face_region,
                           localCsys=None)

