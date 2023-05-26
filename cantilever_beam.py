from abaqus import *
from abaqusConstants import *
import regionToolset

print()

session.viewports['Viewport: 1'].setValues(displayedObject=None)

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
cantileverInstance = cantileverAssembly.Instance(name="Cantilever Instance", part=cantileverPart)

"""Static step is used to simulate load"""
cantileverModel.StaticStep(name="Apply load", previous="Initial", description="Load is applied during this step")

print(cantileverModel.FieldOutputRequest)
