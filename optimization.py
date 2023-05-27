from abaqus import *
from abaqusConstants import *
# from abaqus import getInput, getInputs
from odbAccess import openOdb


# if __name__=="name":

pars = (('VolFrac:', '0.5'), ('Rmin:', '1'), ('ER:', '0.02'))
vf, rmin, ert = [k for k in getInputs(pars, dialogTitle='Create Block')]
print(vf, rmin, ert)
if vf<0 or rmin<0 or ert<0:
    sys.exit()

# mddb = openOdb(getInput('Input CAE file:', default='Test.cae'))

o1 = session.openOdb(name='D:/SIMULIA/Work/Test.odb')
session.viewports['Viewport: 1'].setValues(displayedObject=o1)

##var_list = [k for k in getInput(('Name:', 'abaqus'), dialogTitle="Parameters")]
##print(var_list[0])

# model = mdb.models[mdb.models.keys()[0]]
# part = model.parts["Part-1"]
# print(model.parts.keys())
# part = model.parts(model.parts.keys()[0])