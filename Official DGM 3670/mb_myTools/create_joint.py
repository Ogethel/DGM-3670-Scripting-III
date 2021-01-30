import maya.cmds as cmds

# Steve Code

class CreateJoint:
    def CreateJoints(self):
        sels = cmds.ls(sl=True)
        cmds.select(clear=True)
        cmds.joint(p=(cmds.pointPosition(sels[0])))
        if len(sels) > 0:
            for i in range(1, len(sels)):
                cmds.joint(p=cmds.pointPosition(sels[i]))
                cmds.parent(w=True)


#Clayton's Code

def CJointsFromSels():
    sels = cmds.ls(sl=True)
    jnts = []

    for i in range(len(sels)):
        name = sels[i].rpartition('|')[2].partition('.')[0]
        for suffix in ['_Ctrl', '_Geo', '_Loc']:
            if name.endswith(suffix):
                name = name.rpartition(suffix)[0]
                break
        name += '_Jnt'

        pos = cmds.pointPosition(sels[i])[0]
        cmds.select(clear=True)
        jnt = cmds.joint(n=name, p=pos[1])
        if i > 0:
            cmds.joint(jnts[i-1], e=True, zeroScaleOrient=True, orientJoint='xyz', secondaryAxisOrient='yup')
            cmds.joint(jnt, e=True, orientation=[0, 0, 0])
        jnts.append(jnt)
    cmds.select(jnts, replace=True)
    return jnts



