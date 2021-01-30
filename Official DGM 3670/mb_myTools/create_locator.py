import maya.cmds as cmds

# Clayton had an additional optional return statement


def create_loc():
    sels = cmds.ls(sl=True)

    bbox = cmds.exactWorldBoundingBox(sels)
    x_pos = (bbox[0] + bbox[3])/2
    y_pos = (bbox[1] + bbox[4])/2
    z_pos = (bbox[2] + bbox[5])/2

    locator = cmds.spaceLocator(position=[0, 0, 0])[0]
    cmds.xform(locator, worldSpace=True, translation=[x_pos, y_pos, z_pos])

    cmds.select(locator, r=True)

    return locator