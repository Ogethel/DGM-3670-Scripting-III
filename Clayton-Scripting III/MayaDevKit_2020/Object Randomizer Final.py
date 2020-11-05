import maya.cmds as cmds
import random


# random.seed(1234)


def objectRand(dupNum=5, minX=10, maxX=10, minY=10, maxY=10, minZ=10, maxZ=10):
    selsObjs = cmds.ls(selection=True)
    # objectName = selsObjs[0]
    # insGroupName = cmds.group(empty=True, name=objectName + '_instance_grp#')
    allDupedObjs = []
    for x in range(0, dupNum):
        dupedObjs = cmds.duplicate(selsObjs)
        allDupedObjs.extend(dupedObjs)
        print x

    for i in allDupedObjs:
        cmds.select(i)
        cmds.move(random.uniform(minX, maxX), random.uniform(minY, maxY), random.uniform(minZ, maxZ))
        print i
        # cmds.parent(dupedObjs[0], insGroupName)

    cmds.hide(selsObjs)
    # cmds.xform(insGroupName, centerPivots=True)


# Select Objects and Enter Number of duplicates, then the min and max pairs for x, y, and z for the random range
objectRand(8, -11, 12, -30, 10, -3, 12)