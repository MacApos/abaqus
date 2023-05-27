# -*- coding: mbcs -*-
# Do not delete the following import lines
from abaqus import *
from abaqusConstants import *

# Macro2(my_radius, my_length, my_thickness, my_part, my_string)

def rename():
    import section
    import regionToolset
    import displayGroupMdbToolset as dgm
    import part
    import material
    import assembly
    import step
    import interaction
    import load
    import mesh
    import optimization
    import job
    import sketch
    import visualization
    import xyPlot
    import displayGroupOdbToolset as dgo
    import connectorBehavior
    session.viewports['Viewport: 1'].setValues(displayedObject=None)
    mdb.models.changeKey(fromName='Cantiliver Beam', toName='Model-1')
    session.viewports['Viewport: 1'].setValues(displayedObject=None)
    mdb.models.changeKey(fromName='Model-1', toName='Cantiliver Beam')
    session.viewports['Viewport: 1'].setValues(displayedObject=None)




def Macro1():
    import section
    import regionToolset
    import displayGroupMdbToolset as dgm
    import part
    import material
    import assembly
    import step
    import interaction
    import load
    import mesh
    import optimization
    import job
    import sketch
    import visualization
    import xyPlot
    import displayGroupOdbToolset as dgo
    import connectorBehavior
    a = mdb.models['Cantilever Beam'].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON,
        predefinedFields=ON, connectors=ON, optimizationTasks=OFF,
        geometricRestrictions=OFF, stopConditions=OFF)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Apply Load')
    a = mdb.models['Cantilever Beam'].rootAssembly
    s1 = a.instances['Beam Instance'].faces
    side1Faces1 = s1.getSequenceFromMask(mask=('[#2 ]', ), )
    region = a.Surface(side1Faces=side1Faces1, name='Surf-1')
    mdb.models['Cantilever Beam'].Pressure(name='Uniform Applied Pressure',
        createStepName='Apply Load', region=region, distributionType=UNIFORM,
        field='', magnitude=10.0, amplitude=UNSET)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=8.97341,
        farPlane=12.8737, width=3.12889, height=1.04433, viewOffsetX=-0.632636,
        viewOffsetY=-0.465042)
    a = mdb.models['Cantilever Beam'].rootAssembly
    f1 = a.instances['Beam Instance'].faces
    faces1 = f1.getSequenceFromMask(mask=('[#10 ]', ), )
    region = a.Set(faces=faces1, name='Set-1')
    mdb.models['Cantilever Beam'].EncastreBC(name='Fix one end',
        createStepName='Apply Load', region=region, localCsys=None)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=9.19667,
        farPlane=12.6504, width=1.19154, height=0.3977, viewOffsetX=-1.20862,
        viewOffsetY=-0.750548)
    mdb.save()
    session.viewports['Viewport: 1'].partDisplay.setValues(mesh=ON)
    session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
        meshTechnique=ON)
    session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
        referenceRepresentation=OFF)
    p1 = mdb.models['Cantilever Beam'].parts['Beam']
    session.viewports['Viewport: 1'].setValues(displayedObject=p1)
    p = mdb.models['Cantilever Beam'].parts['Beam']
    s = p.features['Solid extrude-1'].sketch
    mdb.models['Cantilever Beam'].ConstrainedSketch(name='__edit__',
        objectToCopy=s)
    s1 = mdb.models['Cantilever Beam'].sketches['__edit__']
    g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
    s1.setPrimaryObject(option=SUPERIMPOSE)
    p.projectReferencesOntoSketch(sketch=s1,
        upToFeature=p.features['Solid extrude-1'], filter=COPLANAR_EDGES)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=5.14272,
        farPlane=10.2979, width=0.622163, height=0.221212, cameraPosition=(
        0.0276299, 0.00078946, 10.2203), cameraTarget=(0.0276299, 0.00078946,
        0))
    s1.unsetPrimaryObject()
    del mdb.models['Cantilever Beam'].sketches['__edit__']
    elemType1 = mesh.ElemType(elemCode=C3D8R, elemLibrary=STANDARD,
        kinematicSplit=AVERAGE_STRAIN, secondOrderAccuracy=OFF,
        hourglassControl=DEFAULT, distortionControl=DEFAULT)
    elemType2 = mesh.ElemType(elemCode=C3D6, elemLibrary=STANDARD)
    elemType3 = mesh.ElemType(elemCode=C3D4, elemLibrary=STANDARD)
    p = mdb.models['Cantilever Beam'].parts['Beam']
    c = p.cells
    cells = c.getSequenceFromMask(mask=('[#1 ]', ), )
    pickedRegions =(cells, )
    p.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2,
        elemType3))
    p = mdb.models['Cantilever Beam'].parts['Beam']
    p.seedPart(size=0.25, deviationFactor=0.1, minSizeFactor=0.1)
    p = mdb.models['Cantilever Beam'].parts['Beam']
    p.seedPart(size=0.2, deviationFactor=0.1, minSizeFactor=0.1)
    p = mdb.models['Cantilever Beam'].parts['Beam']
    p.seedPart(size=0.2, deviationFactor=0.05, minSizeFactor=0.1)
    p = mdb.models['Cantilever Beam'].parts['Beam']
    p.seedPart(size=0.15, deviationFactor=0.1, minSizeFactor=0.1)
    p = mdb.models['Cantilever Beam'].parts['Beam']
    p.generateMesh()
    a = mdb.models['Cantilever Beam'].rootAssembly
    a.regenerate()
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF,
        predefinedFields=OFF, connectors=OFF)
    mdb.Job(name='CantileverBeamJob', model='Cantilever Beam',
        description='Job simulates a loaded cantilever beam', type=ANALYSIS,
        atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=50,
        memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True,
        explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF,
        modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='',
        scratch='', resultsFormat=ODB)
    mdb.jobs['CantileverBeamJob'].submit(consistencyChecking=OFF)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=8.46964,
        farPlane=13.3774, width=7.13839, height=2.53808, viewOffsetX=0.67754,
        viewOffsetY=-0.036159)
    session.mdbData.summary()
    o3 = session.openOdb(name='C:/temp/CantileverBeamJob.odb')
    session.viewports['Viewport: 1'].setValues(displayedObject=o3)
    session.viewports['Viewport: 1'].makeCurrent()
    session.viewports['Viewport: 1'].view.setValues(nearPlane=8.53509,
        farPlane=13.312, width=6.65242, height=2.22037, viewOffsetX=0.186684,
        viewOffsetY=0.036389)
    session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
        DEFORMED, ))
    session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
        renderStyle=HIDDEN)
    session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
        renderStyle=WIREFRAME)
    session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
        renderStyle=SHADED)
    session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
        deformationScaling=NONUNIFORM)
    session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
        deformationScaling=AUTO)


def Macro2():
    import section
    import regionToolset
    import displayGroupMdbToolset as dgm
    import part
    import material
    import assembly
    import step
    import interaction
    import load
    import mesh
    import optimization
    import job
    import sketch
    import visualization
    import xyPlot
    import displayGroupOdbToolset as dgo
    import connectorBehavior
# -*- coding: mbcs -*-
# Do not delete the following import lines
from abaqus import *
from abaqusConstants import *

# Macro2(my_radius, my_length, my_thickness, my_part, my_string)

def rename():
    import section
    import regionToolset
    import displayGroupMdbToolset as dgm
    import part
    import material
    import assembly
    import step
    import interaction
    import load
    import mesh
    import optimization
    import job
    import sketch
    import visualization
    import xyPlot
    import displayGroupOdbToolset as dgo
    import connectorBehavior
    session.viewports['Viewport: 1'].setValues(displayedObject=None)
    mdb.models.changeKey(fromName='Cantiliver Beam', toName='Model-1')
    session.viewports['Viewport: 1'].setValues(displayedObject=None)
    mdb.models.changeKey(fromName='Model-1', toName='Cantiliver Beam')
    session.viewports['Viewport: 1'].setValues(displayedObject=None)




def Macro1():
    import section
    import regionToolset
    import displayGroupMdbToolset as dgm
    import part
    import material
    import assembly
    import step
    import interaction
    import load
    import mesh
    import optimization
    import job
    import sketch
    import visualization
    import xyPlot
    import displayGroupOdbToolset as dgo
    import connectorBehavior
    a = mdb.models['Cantilever Beam'].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON,
        predefinedFields=ON, connectors=ON, optimizationTasks=OFF,
        geometricRestrictions=OFF, stopConditions=OFF)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Apply Load')
    a = mdb.models['Cantilever Beam'].rootAssembly
    s1 = a.instances['Beam Instance'].faces
    side1Faces1 = s1.getSequenceFromMask(mask=('[#2 ]', ), )
    region = a.Surface(side1Faces=side1Faces1, name='Surf-1')
    mdb.models['Cantilever Beam'].Pressure(name='Uniform Applied Pressure',
        createStepName='Apply Load', region=region, distributionType=UNIFORM,
        field='', magnitude=10.0, amplitude=UNSET)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=8.97341,
        farPlane=12.8737, width=3.12889, height=1.04433, viewOffsetX=-0.632636,
        viewOffsetY=-0.465042)
    a = mdb.models['Cantilever Beam'].rootAssembly
    f1 = a.instances['Beam Instance'].faces
    faces1 = f1.getSequenceFromMask(mask=('[#10 ]', ), )
    region = a.Set(faces=faces1, name='Set-1')
    mdb.models['Cantilever Beam'].EncastreBC(name='Fix one end',
        createStepName='Apply Load', region=region, localCsys=None)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=9.19667,
        farPlane=12.6504, width=1.19154, height=0.3977, viewOffsetX=-1.20862,
        viewOffsetY=-0.750548)
    mdb.save()
    session.viewports['Viewport: 1'].partDisplay.setValues(mesh=ON)
    session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
        meshTechnique=ON)
    session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
        referenceRepresentation=OFF)
    p1 = mdb.models['Cantilever Beam'].parts['Beam']
    session.viewports['Viewport: 1'].setValues(displayedObject=p1)
    p = mdb.models['Cantilever Beam'].parts['Beam']
    s = p.features['Solid extrude-1'].sketch
    mdb.models['Cantilever Beam'].ConstrainedSketch(name='__edit__',
        objectToCopy=s)
    s1 = mdb.models['Cantilever Beam'].sketches['__edit__']
    g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
    s1.setPrimaryObject(option=SUPERIMPOSE)
    p.projectReferencesOntoSketch(sketch=s1,
        upToFeature=p.features['Solid extrude-1'], filter=COPLANAR_EDGES)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=5.14272,
        farPlane=10.2979, width=0.622163, height=0.221212, cameraPosition=(
        0.0276299, 0.00078946, 10.2203), cameraTarget=(0.0276299, 0.00078946,
        0))
    s1.unsetPrimaryObject()
    del mdb.models['Cantilever Beam'].sketches['__edit__']
    elemType1 = mesh.ElemType(elemCode=C3D8R, elemLibrary=STANDARD,
        kinematicSplit=AVERAGE_STRAIN, secondOrderAccuracy=OFF,
        hourglassControl=DEFAULT, distortionControl=DEFAULT)
    elemType2 = mesh.ElemType(elemCode=C3D6, elemLibrary=STANDARD)
    elemType3 = mesh.ElemType(elemCode=C3D4, elemLibrary=STANDARD)
    p = mdb.models['Cantilever Beam'].parts['Beam']
    c = p.cells
    cells = c.getSequenceFromMask(mask=('[#1 ]', ), )
    pickedRegions =(cells, )
    p.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2,
        elemType3))
    p = mdb.models['Cantilever Beam'].parts['Beam']
    p.seedPart(size=0.25, deviationFactor=0.1, minSizeFactor=0.1)
    p = mdb.models['Cantilever Beam'].parts['Beam']
    p.seedPart(size=0.2, deviationFactor=0.1, minSizeFactor=0.1)
    p = mdb.models['Cantilever Beam'].parts['Beam']
    p.seedPart(size=0.2, deviationFactor=0.05, minSizeFactor=0.1)
    p = mdb.models['Cantilever Beam'].parts['Beam']
    p.seedPart(size=0.15, deviationFactor=0.1, minSizeFactor=0.1)
    p = mdb.models['Cantilever Beam'].parts['Beam']
    p.generateMesh()
    a = mdb.models['Cantilever Beam'].rootAssembly
    a.regenerate()
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF,
        predefinedFields=OFF, connectors=OFF)
    mdb.Job(name='CantileverBeamJob', model='Cantilever Beam',
        description='Job simulates a loaded cantilever beam', type=ANALYSIS,
        atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=50,
        memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True,
        explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF,
        modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='',
        scratch='', resultsFormat=ODB)
    mdb.jobs['CantileverBeamJob'].submit(consistencyChecking=OFF)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=8.46964,
        farPlane=13.3774, width=7.13839, height=2.53808, viewOffsetX=0.67754,
        viewOffsetY=-0.036159)
    session.mdbData.summary()
    o3 = session.openOdb(name='C:/temp/CantileverBeamJob.odb')
    session.viewports['Viewport: 1'].setValues(displayedObject=o3)
    session.viewports['Viewport: 1'].makeCurrent()
    session.viewports['Viewport: 1'].view.setValues(nearPlane=8.53509,
        farPlane=13.312, width=6.65242, height=2.22037, viewOffsetX=0.186684,
        viewOffsetY=0.036389)
    session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
        DEFORMED, ))
    session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
        renderStyle=HIDDEN)
    session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
        renderStyle=WIREFRAME)
    session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
        renderStyle=SHADED)
    session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
        deformationScaling=NONUNIFORM)
    session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
        deformationScaling=AUTO)


    Mdb()
    session.viewports['Viewport: 1'].setValues(displayedObject=None)
    mdb.models.changeKey(fromName='Model-1', toName='Cantilever Beam')
    session.viewports['Viewport: 1'].setValues(displayedObject=None)
    s = mdb.models['Cantilever Beam'].ConstrainedSketch(name='__profile__',
        sheetSize=200.0)
    g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
    s.setPrimaryObject(option=STANDALONE)
    s.rectangle(point1=(0.1, 0.1), point2=(0.3, -0.1))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=185.624,
        farPlane=191.5, width=18.8204, height=8.46339, cameraPosition=(1.63278,
        2.42903, 188.562), cameraTarget=(1.63278, 2.42903, 0))
    s.rectangle(point1=(-2.16999959945679, 3.41750144958496), point2=(
        0.458342671394348, -0.440906524658203))
    s.undo()
    session.viewports['Viewport: 1'].view.setValues(nearPlane=188.305,
        farPlane=188.818, width=1.64404, height=0.739313, cameraPosition=(
        0.560934, 0.157243, 188.562), cameraTarget=(0.560934, 0.157243, 0))
    p = mdb.models['Cantilever Beam'].Part(name='Beam', dimensionality=THREE_D,
        type=DEFORMABLE_BODY)
    p = mdb.models['Cantilever Beam'].parts['Beam']
    p.BaseSolidExtrude(sketch=s, depth=5.0)
    s.unsetPrimaryObject()
    p = mdb.models['Cantilever Beam'].parts['Beam']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    del mdb.models['Cantilever Beam'].sketches['__profile__']
    mdb.saveAs(pathName='C:/temp/cantilever_macro')
    session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON,
        engineeringFeatures=ON)
    session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
        referenceRepresentation=OFF)
    mdb.models['Cantilever Beam'].Material(name='AISI 1005 Steel')
    mdb.models['Cantilever Beam'].materials['AISI 1005 Steel'].Density(table=((
        7872.0, ), ))
    mdb.models['Cantilever Beam'].materials['AISI 1005 Steel'].Elastic(table=((
        200000000000.0, 0.29), ))
    mdb.models['Cantilever Beam'].HomogeneousSolidSection(name='Beam-Section',
        material='AISI 1005 Steel', thickness=None)
    p = mdb.models['Cantilever Beam'].parts['Beam']
    c = p.cells
    cells = c.getSequenceFromMask(mask=('[#1 ]', ), )
    region = p.Set(cells=cells, name='Set-1')
    p = mdb.models['Cantilever Beam'].parts['Beam']
    p.SectionAssignment(region=region, sectionName='Beam-Section', offset=0.0,
        offsetType=MIDDLE_SURFACE, offsetField='',
        thicknessAssignment=FROM_SECTION)
    a = mdb.models['Cantilever Beam'].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(
        optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
    a = mdb.models['Cantilever Beam'].rootAssembly
    a.DatumCsysByDefault(CARTESIAN)
    p = mdb.models['Cantilever Beam'].parts['Beam']
    a.Instance(name='Beam-1', part=p, dependent=ON)
    mdb.models['Cantilever Beam'].rootAssembly.features.changeKey(
        fromName='Beam-1', toName='Beam Instance')
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(
        adaptiveMeshConstraints=ON)
    mdb.models['Cantilever Beam'].StaticStep(name='Apply load', previous='Initial',
        description='Load is applied during this step')
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(
        step='Apply load')
    mdb.models['Cantilever Beam'].fieldOutputRequests['F-Output-1'].suppress()
    mdb.models['Cantilever Beam'].fieldOutputRequests['F-Output-1'].resume()
    mdb.models['Cantilever Beam'].fieldOutputRequests['F-Output-1'].setValues(
        variables=('S', 'PEMAG', 'U', 'RF', 'CF'))
    mdb.models['Cantilever Beam'].fieldOutputRequests.changeKey(
        fromName='F-Output-1', toName='Selected FIeld Outputs')
    mdb.models['Cantilever Beam'].historyOutputRequests.changeKey(
        fromName='H-Output-1', toName='Deafult History Outputs')
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON,
        predefinedFields=ON, connectors=ON, adaptiveMeshConstraints=OFF)
    a = mdb.models['Cantilever Beam'].rootAssembly
    s1 = a.instances['Beam Instance'].faces
    side1Faces1 = s1.getSequenceFromMask(mask=('[#8 ]', ), )
    region = a.Surface(side1Faces=side1Faces1, name='Surf-1')
    mdb.models['Cantilever Beam'].Pressure(name='Uniform applied pressure',
        createStepName='Apply load', region=region, distributionType=UNIFORM,
        field='', magnitude=10.0, amplitude=UNSET)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Initial')
    a = mdb.models['Cantilever Beam'].rootAssembly
    f1 = a.instances['Beam Instance'].faces
    faces1 = f1.getSequenceFromMask(mask=('[#10 ]', ), )
    region = a.Set(faces=faces1, name='Set-1')
    mdb.models['Cantilever Beam'].EncastreBC(name='Encastre one end',
        createStepName='Initial', region=region, localCsys=None)
    mdb.save()
    session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF,
        engineeringFeatures=OFF, mesh=ON)
    session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
        meshTechnique=ON)
    p1 = mdb.models['Cantilever Beam'].parts['Beam']
    session.viewports['Viewport: 1'].setValues(displayedObject=p1)
    elemType1 = mesh.ElemType(elemCode=C3D8R, elemLibrary=STANDARD,
        kinematicSplit=AVERAGE_STRAIN, secondOrderAccuracy=OFF,
        hourglassControl=DEFAULT, distortionControl=DEFAULT)
    elemType2 = mesh.ElemType(elemCode=C3D6, elemLibrary=STANDARD)
    elemType3 = mesh.ElemType(elemCode=C3D4, elemLibrary=STANDARD)
    p = mdb.models['Cantilever Beam'].parts['Beam']
    c = p.cells
    cells = c.getSequenceFromMask(mask=('[#1 ]', ), )
    pickedRegions =(cells, )
    p.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2,
        elemType3))
    p = mdb.models['Cantilever Beam'].parts['Beam']
    p.seedPart(size=0.2, deviationFactor=0.1, minSizeFactor=0.1)
    p = mdb.models['Cantilever Beam'].parts['Beam']
    p.generateMesh()
    p = mdb.models['Cantilever Beam'].parts['Beam']
    p.deleteMesh()
    p = mdb.models['Cantilever Beam'].parts['Beam']
    p.seedPart(size=0.1, deviationFactor=0.1, minSizeFactor=0.1)
    p = mdb.models['Cantilever Beam'].parts['Beam']
    p.generateMesh()
    mdb.save()
    a = mdb.models['Cantilever Beam'].rootAssembly
    a.regenerate()
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF,
        predefinedFields=OFF, connectors=OFF)
    mdb.Job(name='CantileverBeamJob', model='Cantilever Beam',
        description='Job simulates a loaded cantilever beam', type=ANALYSIS,
        atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=60,
        memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True,
        explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF,
        modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='',
        scratch='', resultsFormat=ODB)
    mdb.save()
    mdb.save()
    mdb.jobs['CantileverBeamJob'].submit(consistencyChecking=OFF)
    session.mdbData.summary()
    o3 = session.openOdb(name='C:/temp/CantileverBeamJob.odb')
    session.viewports['Viewport: 1'].setValues(displayedObject=o3)
    session.viewports['Viewport: 1'].makeCurrent()
    session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
        DEFORMED, ))
    session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
        UNDEFORMED, ))
    session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
        CONTOURS_ON_DEF, ))


def encastre_bc():
    import section
    import regionToolset
    import displayGroupMdbToolset as dgm
    import part
    import material
    import assembly
    import step
    import interaction
    import load
    import mesh
    import optimization
    import job
    import sketch
    import visualization
    import xyPlot
    import displayGroupOdbToolset as dgo
    import connectorBehavior
    a = mdb.models['Cantilever Beam'].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    a = mdb.models['Cantilever Beam'].rootAssembly
    f1 = a.instances['Cantilever Instance'].faces
    faces1 = f1.getSequenceFromMask(mask=('[#10 ]', ), )
    region = a.Set(faces=faces1, name='Set-1')
    mdb.models['Cantilever Beam'].EncastreBC(name='One end fixed', 
        createStepName='Initial', region=region, localCsys=None)


def veiwport():
    import section
    import regionToolset
    import displayGroupMdbToolset as dgm
    import part
    import material
    import assembly
    import step
    import interaction
    import load
    import mesh
    import optimization
    import job
    import sketch
    import visualization
    import xyPlot
    import displayGroupOdbToolset as dgo
    import connectorBehavior
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Initial')


def select_face():
    import section
    import regionToolset
    import displayGroupMdbToolset as dgm
    import part
    import material
    import assembly
    import step
    import interaction
    import load
    import mesh
    import optimization
    import job
    import sketch
    import visualization
    import xyPlot
    import displayGroupOdbToolset as dgo
    import connectorBehavior
    session.viewports['Viewport: 1'].view.setValues(nearPlane=355.828, 
        farPlane=532.191, width=190.087, height=91.1592, cameraUpVector=(
        -0.503614, 0.572908, -0.646645), cameraTarget=(9.16525, 4.5582, 
        108.777))


def test():
    import section
    import regionToolset
    import displayGroupMdbToolset as dgm
    import part
    import material
    import assembly
    import step
    import interaction
    import load
    import mesh
    import optimization
    import job
    import sketch
    import visualization
    import xyPlot
    import displayGroupOdbToolset as dgo
    import connectorBehavior
    session.viewports['Viewport: 1'].view.setValues(nearPlane=356.277, 
        farPlane=531.741, width=190.327, height=91.2745, cameraPosition=(
        265.514, 260.907, 365.125), cameraUpVector=(-0.687794, 0.565536, 
        -0.455092), cameraTarget=(9.16525, 4.5582, 108.777))


def view_load():
    import section
    import regionToolset
    import displayGroupMdbToolset as dgm
    import part
    import material
    import assembly
    import step
    import interaction
    import load
    import mesh
    import optimization
    import job
    import sketch
    import visualization
    import xyPlot
    import displayGroupOdbToolset as dgo
    import connectorBehavior
    session.viewports['Cantilever Beam Example'].assemblyDisplay.setValues(
        step='Apply load')


def save():
    import section
    import regionToolset
    import displayGroupMdbToolset as dgm
    import part
    import material
    import assembly
    import step
    import interaction
    import load
    import mesh
    import optimization
    import job
    import sketch
    import visualization
    import xyPlot
    import displayGroupOdbToolset as dgo
    import connectorBehavior
    mdb.saveAs(pathName='D:/SIMULIA/Work/Test.cae')


