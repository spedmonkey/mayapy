import maya.standalone
# Start Maya in batch mode
maya.standalone.initialize() 

#continue with your script, using the normal
import maya.cmds as cmds

cmds.file("C:/test.ma", open=True )
#cmds.file(crename='myTest_v02.ma')
cmds.file(rename="C:/myTest_v02.ma")
print 'file renamed'
cmds.polyCube()
cmds.polySphere()
print 'cube created'
cmds.file(save=True)
