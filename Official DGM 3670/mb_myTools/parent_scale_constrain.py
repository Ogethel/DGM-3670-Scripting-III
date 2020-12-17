import maya.cmds as cmds


def parent_constrain():

    sels = cmds.ls(sl=True)

    if len(sels) % 2 == 1:
        cmds.error('One too many or one too few items selected')

    sels_count = len(sels)

    # print sels_count

    for i in range(0, sels_count, 2):
        # print 'I want to constrain sels %s to %s' % (sels[i+1], sels[i])
        cmds.parentConstraint(sels[i+1], sels[i], maintainOffset=False)
        cmds.scaleConstraint(sels[i + 1], sels[i], maintainOffset=False)