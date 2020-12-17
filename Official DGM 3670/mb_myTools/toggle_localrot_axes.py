import maya.cmds as cmds


def toggle_attr():

    sels = cmds.ls(sl=True)

    for i in sels:
        cmds.setAttr(i + ".displayLocalAxis", k=True)
        cmds.setAttr(i + ".jointOrientX", k=True)
        cmds.setAttr(i + ".jointOrientY", k=True)
        cmds.setAttr(i + ".jointOrientZ", k=True)

        cmds.toggle(i, la=True)
