from abaqus import *
# from abaqusConstants import *
#
#
# ##if "Model-01" in mdb.models:
# ##    mdb.models.changeKey(fromName='Model-01', toName='Cantiliver)
# print()
# if not mdb.models.keys()[0]=='Cantilever Beam':
#     mdb.models.changeKey(fromName=mdb.models.keys()[0], toName='Cantilever Beam')
#
# beamModel = mdb.models['Cantilever Beam']
#
# import sketch
# import part
#
# beamProfileSketch = beamModel.ConstrainedSketch(name='Beam profile', sheetSize=5)
# beamProfileSketch.rectangle(point1=(-0.15,-0.05), point2=(0.15, 0.05))
#
# beamPart = beamModel.Part(name="Beam", dimensionality=THREE_D, type=DEFORMABLE_BODY)
# beamPart.BaseSolidExtrude(sketch=beamProfileSketch, depth=5)
#
# beamMaterial = beamModel.Material(name = "AISI 1005 Steel")
# beamMaterial.Density(table=((7872, ),  )) #kg/m^3
# beamMaterial.Elastic(table=((200E9, 0.29), ))
#
# beamSection = beamModel.HomogeneousSolidSection(name = "Beam Section", material="AISI 1005 Steel")
#
# # Assign beam to this section
# beamRegion = (beamPart.cells, )
# beamPart.SectionAssignment(region = beamRegion, sectionName="Beam Section")
