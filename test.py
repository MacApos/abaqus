from abaqus import *

myViewport = session.Viewport(name='Cantilever Beam Example',
    origin=(20, 20), width=150, height=120)

##print(session.viewports)

for i in range(len(session.viewports.keys())):
    print(session.viewports.keys()[i])

##print(type(session.viewports.keys()))

