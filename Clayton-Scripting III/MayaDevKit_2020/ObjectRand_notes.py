import maya.cmds as cmds
import random

random.seed(1234)

# def rngObjs(dupnum, maxX, maxY, maxZ):
#     selected = cmds.ls(selection=True)
#     dupedObjects =[]
#     for s in range(0, 3):
#         dupeObjs = cmds.duplicate(selected)
#         dupedObjects.append()
#
#         for i in dupeObjs:
#             cmds.move(random.uniform(0, 2), random.uniform(0, 2), random.uniform(0, 2))
#
# print rngObjs(5, 3, 2, 5)

# Python script Example

'''
cubeList = cmds.ls('myCube*')
if len( cubeList ) > 0:
    cmds.delete( cubeList )
'''


def objectRand(dupNum=5, maxX=10, maxY=10, maxZ=10):
    selsObjs = cmds.ls(selection=True)
    objectName = selsObjs[0]
    insGroupName = cmds.group(empty=True, nam=objectName + '_instance_grp#')
    allDupedObjs = []
    for x in range(0, dupNum):
        dupedObjs = cmds.duplicate(selsObjs)
        allDupedObjs.extent(dupedObjs)

        for i in dupedObjs:
            cmds.move(random.uniform(0, maxX), random.uniform(0, maxY), random.uniform(0, maxZ))

    cmds.hide(selsObjs)
    cmds.xform(insGroupName, centerPivots=True)


result = cmds.polyCube(w=1, h=1, d=1, name='myObject#')

# print 'result: ' + str( result )

transformName = result[0]

instanceGroupName = cmds.group(empty=True, name=transformName + '_instance_grp#')

for i in range(0, 50):
    instanceResult = cmds.instance(transformName, name=transformName + '_instance#')
    # print 'instanceResult: ' + str(instanceResult)

    cmds.parent(instanceResult, instanceGroupName)

    x = random.uniform(-10, 10)
    y = random.uniform(0, 20)
    z = random.uniform(-10, 10)

    cmds.move(x, y, z, instanceResult)

cmds.hide(transformName)

cmds.xform(instanceGroupName, centerPivots=True)
