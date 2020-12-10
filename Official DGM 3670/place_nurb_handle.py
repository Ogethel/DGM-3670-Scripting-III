import maya.cmds as cmds

selection = cmds.ls(selection=True)

for i in selection:
    control_object = cmds.circle(name=i + "_anim", radius=25)[0]
    offset_group = cmds.group(empty=True, name=control_object + "_grp")
    cmds.parent(control_object, offset_group)
    contraint = cmds.parentConstraint(i, offset_group, maintainOffset=False)
    cmds.delete(contraint)
    cmds.parentConstraint(control_object, i, maintainOffset=False)