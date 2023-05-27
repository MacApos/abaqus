#
# Getting Started with Abaqus: Interactive Edition
#
# Script for stiffened plate example
#
from abaqus import *
from abaqusConstants import *
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
session.journalOptions.setValues(replayGeometry=COORDINATE,
    recoverGeometry=COORDINATE)
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
Mdb()

s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=5.0)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=STANDALONE)
s.Line(point1=(-0.65, 0.075), point2=(0.725000000046566, 0.075))
s.HorizontalConstraint(entity=g.findAt((0.0375, 0.075)), addUndoState=False)
s.Line(point1=(-0.325, 0.075), point2=(-0.325, 0.225000000046566))
s.VerticalConstraint(entity=g.findAt((-0.325, 0.15)), addUndoState=False)
s.PerpendicularConstraint(entity1=g.findAt((0.0375, 0.075)), entity2=g.findAt(
    (-0.325, 0.15)), addUndoState=False)
s.CoincidentConstraint(entity1=v.findAt((-0.325, 0.075)), entity2=g.findAt((
    0.0375, 0.075)), addUndoState=False)
s.Line(point1=(0.15, 0.075), point2=(0.15, 0.25))
s.VerticalConstraint(entity=g.findAt((0.15, 0.1625)), addUndoState=False)
s.PerpendicularConstraint(entity1=g.findAt((0.0375, 0.075)), entity2=g.findAt(
    (0.15, 0.1625)), addUndoState=False)
s.CoincidentConstraint(entity1=v.findAt((0.15, 0.075)), entity2=g.findAt((
    0.0375, 0.075)), addUndoState=False)
s.Line(point1=(0.55, 0.075), point2=(0.55, 0.25))
s.VerticalConstraint(entity=g.findAt((0.55, 0.1625)), addUndoState=False)
s.PerpendicularConstraint(entity1=g.findAt((0.0375, 0.075)), entity2=g.findAt(
    (0.55, 0.1625)), addUndoState=False)
s.CoincidentConstraint(entity1=v.findAt((0.55, 0.075)), entity2=g.findAt((
    0.0375, 0.075)), addUndoState=False)
s.EqualLengthConstraint(entity1=g.findAt((-0.325, 0.15)), entity2=g.findAt((
    0.15, 0.1625)))
s.EqualLengthConstraint(entity1=g.findAt((0.15, 0.15625)), entity2=g.findAt((
    0.55, 0.1625)), addUndoState=False)
s.ObliqueDimension(
    vertex1=v.findAt((-0.325, 0.075)), vertex2=v.findAt((-0.325,
    0.225)), textPoint=(-0.829278707504272, 0.192073285579681), value=0.1)
s.move(vector=(0.0, 0.025), objectList=(g.findAt((0.0375, 0.075)), g.findAt((
    -0.325, 0.125)), g.findAt((0.15, 0.125)), g.findAt((0.55, 0.125))))
s.breakCurve(curve1=g.findAt((0.0375, 0.1)), point1=(-0.441734611988068,
    0.0968574285507202), curve2=g.findAt((-0.325, 0.15)), point2=(
    -0.326785087585449, 0.149390280246735))
s.breakCurve(curve1=g.findAt((0.2, 0.1)), point1=(0.00492632389068604,
    0.106707394123077), curve2=g.findAt((0.15, 0.15)), point2=(
    0.152718663215637, 0.155956923961639))
s.breakCurve(curve1=g.findAt((0.4375, 0.1)), point1=(0.415460348129272,
    0.100140750408173), curve2=g.findAt((0.55, 0.15)), point2=(
    0.556684136390686, 0.139540374279022))
s.HorizontalDimension(vertex1=v.findAt((-0.65, 0.1)), vertex2=v.findAt((0.725,
    0.1)), textPoint=(0.458155989646912, -0.165806710720062), value=2.0)
s.FixedConstraint(entity=g.findAt((0.15, 0.15)))
s.EqualLengthConstraint(entity1=g.findAt((-0.8, 0.1)), entity2=g.findAt((
    -0.0875, 0.1)))
s.delete(objectList=(c[34], ))
s.EqualLengthConstraint(entity1=g.findAt((-0.0875, 0.1)), entity2=g.findAt((
    0.35, 0.1)), addUndoState=False)
s.EqualLengthConstraint(entity1=g.findAt((0.3125, 0.1)), entity2=g.findAt((
    0.9125, 0.1)), addUndoState=False)
s.move(vector=(0.0375, 0.0), objectList=(g.findAt((-0.325, 0.15)), g.findAt((
    0.175, 0.15)), g.findAt((0.675, 0.15)), g.findAt((-0.575, 0.1)), g.findAt((
    -0.075, 0.1)), g.findAt((0.425, 0.1)), g.findAt((0.925, 0.1))))
s.move(
    vector=(-0.2125, -0.1),
    objectList=(
           g.findAt((-0.2875, 0.15)), g.findAt((0.2125, 0.15)),
           g.findAt((0.7125, 0.15)), g.findAt((-0.5375, 0.1)),
           g.findAt((-0.0375, 0.1)), g.findAt((0.4625, 0.1)),
           g.findAt((0.9625, 0.1))))
p = mdb.models['Model-1'].Part(name='Plate', dimensionality=THREE_D,
    type=DEFORMABLE_BODY)
p = mdb.models['Model-1'].parts['Plate']
p.BaseShellExtrude(sketch=s, depth=2.0)
s.unsetPrimaryObject()
p = mdb.models['Model-1'].parts['Plate']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
del mdb.models['Model-1'].sketches['__profile__']


session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].partDisplay.setValues(renderStyle=SHADED)

mdb.models['Model-1'].Material('Steel')
mdb.models['Model-1'].materials['Steel'].Density(table=((7800.0, ), ))
mdb.models['Model-1'].materials['Steel'].Elastic(table=((210.0E9, 0.3), ))
mdb.models['Model-1'].materials['Steel'].Plastic(table=((300.0E6, 0.0),
    (350.0E6, 0.025), (375.0E6, 0.1), (394.0E6, 0.2), (400.0E6, 0.35)))

mdb.models['Model-1'].HomogeneousShellSection(name='PlateSection',
    preIntegrate=OFF, material='Steel', thickness=0.025,
    poissonDefinition=DEFAULT, temperature=GRADIENT,
    integrationRule=SIMPSON, numIntPts=5)
mdb.models['Model-1'].HomogeneousShellSection(name='StiffSection',
    preIntegrate=OFF, material='Steel', thickness=0.0125,
    poissonDefinition=DEFAULT, temperature=GRADIENT,
    integrationRule=SIMPSON, numIntPts=5)

f = p.faces
faces = f.findAt(
    ((0.833333, 0.0, 1.333333), ),
    ((0.333333, 0.0, 1.333333), ),
    ((-0.166667, 0.0, 1.333333), ),
    ((-0.666667, 0.0, 1.333333), ))
region =(None, None, faces, None)
p.SectionAssignment(region=region, sectionName='PlateSection', offset=-0.5)

faces = f.findAt(
    ((-0.5, 0.066669, 1.333333), ),
    ((0.0, 0.066671, 1.333333), ),
    ((0.5, 0.066673, 1.333333), ))
region =(None, None, faces, None)

p.SectionAssignment(region=region, sectionName='StiffSection')

a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)

a.DatumCsysByDefault(CARTESIAN)
a.Instance(name='Plate-1', part=p, dependent=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(renderStyle=SHADED)

p = mdb.models['Model-1'].parts['Plate']
e = p.edges
pickedEdges = e.findAt(((0.0, 0.0, 0.5), ))
p.PartitionEdgeByParam(edges=pickedEdges, parameter=0.5)

v = a.instances['Plate-1'].vertices
verts = v.findAt(((0.0, 0.0, 1.0), ))
a.Set(vertices=verts, name='Center')

e = a.instances['Plate-1'].edges
edges = e.findAt(
    ((0.875, 0.0, 2.0), ), ((0.625, 0.0, 0.0), ),
    ((1.0, 0.0, 0.5), ), ((0.375, 0.0, 2.0), ),
    ((0.125, 0.0, 0.0), ), ((-0.125, 0.0, 2.0), ),
    ((-0.375, 0.0, 0.0), ), ((-0.625, 0.0, 2.0), ),
    ((-1.0, 0.0, 0.5), ), ((-0.875, 0.0, 0.0), ))
a.Set(edges=edges, name='Edge')

session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF,
    predefinedFields=OFF)

mdb.models['Model-1'].ExplicitDynamicsStep(name='Blast', previous='Initial',
    description='Apply blast loading', timePeriod=0.05, adiabatic=OFF,
    timeIncrementationMethod=AUTOMATIC_GLOBAL, scaleFactor=1,
    maxIncrement=None, massScaling=PREVIOUS_STEP, linearBulkViscosity=0.06,
    quadBulkViscosity=1.2)

regionDef=a.sets['Center']
mdb.models['Model-1'].steps['Blast'].Monitor(dof=2, node=regionDef)

mdb.models['Model-1'].fieldOutputRequests['F-Output-1'].setValues(
    numIntervals=25)

mdb.models['Model-1'].historyOutputRequests['H-Output-1'].setValues(
    numIntervals=500)

regionDef=mdb.models['Model-1'].rootAssembly.sets['Center']
mdb.models['Model-1'].HistoryOutputRequest(name='Center-U2',
    createStepName='Blast', variables=('U2', ), numIntervals=500,
    region=regionDef)

session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON,
    predefinedFields=ON)

region = a.sets['Edge']
mdb.models['Model-1'].EncastreBC(name='Fix edges', createStepName='Initial',
    region=region)
mdb.models['Model-1'].TabularAmplitude(name='Blast', timeSpan=STEP,
    smooth=0.25, data=((0.0, 0.0), (0.001, 7.0E5), (0.01, 7.0E5),
    (0.02, 0.0), (0.05, 0.0)))

s = a.instances['Plate-1'].faces
side1Faces = s.findAt(
    ((0.833333, 0.0, 1.333333), ),
    ((0.333333, 0.0, 1.333333), ),
    ((-0.166667, 0.0, 1.333333), ),
    ((-0.666667, 0.0, 1.333333), ))
region = regionToolset.Region(side1Faces=side1Faces)
mdb.models['Model-1'].Pressure(name='Pressure load', createStepName='Blast',
    region=region, magnitude=1.0, amplitude='Blast')

session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=ON)
p.seedPart(size=0.1)

e = p.edges
edges =(e.findAt(coordinates=(-0.5, 0.025, 2.0)), e.findAt(coordinates=(
    0.0, 0.025, 2.0)), e.findAt(coordinates=(0.5, 0.025, 2.0)), e.findAt(
    coordinates=(-0.5, 0.075, 0.0)), e.findAt(coordinates=(0.0, 0.075,
    0.0)), e.findAt(coordinates=(0.5, 0.075, 0.0)))
p.seedEdgeByNumber(edges=edges, number=2)

elemType1 = mesh.ElemType(elemCode=S4R, elemLibrary=EXPLICIT,
    hourglassControl=RELAX_STIFFNESS)
elemType2 = mesh.ElemType(elemCode=S3, elemLibrary=EXPLICIT)

f = p.faces
faces = f

regions =(None, None, faces, None)
p.setElementType(regions=regions, elemTypes=(elemType1, elemType2))

pickedRegions = f
p.setMeshControls(regions=pickedRegions, elemShape=QUAD, algorithm=MEDIAL_AXIS)

p.generateMesh()

session.viewports['Viewport: 1'].assemblyDisplay.setValues(renderStyle=SHADED)

mdb.Job(name='BlastLoad', model='Model-1')
mdb.jobs['BlastLoad'].setValues(description='Blast load on a flat plate with stiffeners: S4R elements (20x20 mesh) Normal stiffeners (20x2)')

a.regenerate()

mdb.saveAs('StiffPlate')