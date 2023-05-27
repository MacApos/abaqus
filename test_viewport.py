from abaqus import *

if mdb.models.keys()[0] != "Cantilever Beam":
    mdb.models.changeKey(fromName=mdb.models.keys()[0], toName="Cantilever Beam")

cantileverModel = mdb.models["Cantilever Beam"]

session.viewports['Viewport: 1'].setValues(displayedObject=None)

# myViewport = session.Viewport(name='Cantilever Beam Example',
#     origin=(20, 20), width=150, height=120)

#defaultViewport = session.Viewport(name=session.viewports.keys()[0])

##if session.viewports.keys()[0] != "New Viewport":
##    print(session.viewports.keys()[i])
###    session.viewports.changeKeys(fromName=session.viewports.keys()[0], toName="New Viewport")


##print(session.viewports)

##for i in range(len(session.viewports.keys())):
##    print(session.viewports.keys()[i])

##print(type(session.viewports.keys()))

