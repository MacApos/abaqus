from abaqus import *
import math
#import CustomKernel
from odbAccess import openOdb
from abaqus import getInput, getInputs

mdl = mdb.Model("Model-1")
#part = mdl.parts["Part-1"]
mdl.Material('Material-01').Elastic(((1.0, 0.3),))
mdl.HomogeneousSolidSection('sldSec', 'Material-01')
mdl.Material('Material-01').Elastic(((0.001**3, 0.3),))
mdl.HomogeneousSolidSection('voidSec', 'Material-02')

