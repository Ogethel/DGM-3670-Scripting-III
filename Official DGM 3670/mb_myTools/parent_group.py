import maya.cmds as cmds


def parent_group_sel():

    selection = cmds.ls(selection=True)

    for i in selection:
        new_group = cmds.group(em=True, name=i + "_grp")
        cmds.matchTransform(new_group, i)
        cmds.parent(i, new_group)

        # offset_group = cmds.group(i, name=i + "_grp", p='null1')
        # cmds.matchTransform(offset_group, i)
        # temp_con = cmds.parentConstraint(i, offset_group, maintainOffset=True)
        # cmds.delete(temp_con)
        cmds.makeIdentity(i, apply=True, t=1, r=1, s=1, n=0)


# parent_group_sel()

# sels = cmds.ls(sl=True)
#
# for i in sels:
#     obj_name = sels[i].name
#     print obj_name
#     cmds.group('%s' % obj_name, name='%s%s%s' % (obj_name, _, sels[i]))
#     cmds.matchTransform(obj_name + '_' + i, obj_name)
#     cmds.parent(obj_name + '_' + i, obj_name)
#
# cmds.polySphere(n='Bone_1', ax=[0, 1, 0], r=1, sx=20, sy=20, cuv=2, ch=1)
#
# cmds.circle(n='Nurb_1', c=[0, 0, 0], nr=[0, 1, 0], sw=360, r=1, d=3, ut=0, tol=0.01, s=8, ch=1)
#
# cmds.group('Nurb_1', name='Nurb_Grp1')
#
# cmds.matchTransform('Nurb_Grp1', 'Bone_1')
#
# cmds.parent('Bone_1', 'Nurb_Grp1')
#  cmds.group('Nurb_1', parent='Bone_1')

