# FK pos and rot. First select controlobject then a joint by Niclas Halvarsson
import maya.cmds as mc

my_sel = mc.ls(sl=True)

if len(my_sel) < 2 or len(my_sel) > 3:
    mc.error("Please select atleast 1 ctrlCurve and 1 joints")

ctl_og = mc.group(empty=True)
mc.parent(my_sel[0], my_sel[1])
mc.parent(ctl_og, my_sel[1])

axis = ["x", "y", "z"]
for i in axis:
    mc.setAttr(my_sel[0] + ".t" + i, 0)
    mc.setAttr(my_sel[0] + ".r" + i, 0)
    mc.setAttr(ctl_og + ".t" + i, 0)
    mc.setAttr(ctl_og + ".r" + i, 0)

mc.parent(ctl_og, w=True)
mc.parent(my_sel[0], ctl_og)

newname = mc.rename(my_sel[0], my_sel[1] + "_CTL")
grpname = newname.split("_CTL")[0]
og_name = mc.rename(ctl_og, grpname + "_OG")

mc.parentConstraint(newname, my_sel[1], mo=False)
if len(my_sel) == 3:
    mc.parentConstraint(my_sel[2], og_name, mo=True)


