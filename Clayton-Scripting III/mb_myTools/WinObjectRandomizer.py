import maya.cmds as cmds
import ObjectRandomizer


def createObjectRandWin():
    window = cmds.window(title="MB-Randomize Objects", widthHeight=(300, 400))
    cmds.columnLayout(columnAttach=('both', 5), rowSpacing=5, adjustableColumn=True)

    cmds.text(label='Input Number of Duplicates')
    num_dups = cmds.intField()

    cmds.intField(num_dups, edit=True)

    cmds.text(label='Input Min X Possible Position')
    min_x = cmds.intField()

    cmds.intField(min_x, edit=True)

    cmds.text(label='Input Max X Possible Position')
    max_x = cmds.intField()

    cmds.intField(max_x, edit=True)

    cmds.text(label='Input Min Y Possible Position')
    min_y = cmds.intField()

    cmds.intField(min_y, edit=True)

    cmds.text(label='Input Max Y Possible Position')
    max_y = cmds.intField()

    cmds.intField(max_y, edit=True)

    cmds.text(label='Input Min Z Possible Position')
    min_z = cmds.intField()

    cmds.intField(min_z, edit=True)

    cmds.text(label='Input Max Z Possible Position')
    max_z = cmds.intField()

    cmds.intField(max_z, edit=True)

    def click(value):
        dorandomize_func(num_dups, min_x, max_x, min_y, max_y, min_z, max_z)

    cmds.button(label='Randomize Objects!', command=click)

    closeCmd = 'cmds.deleteUI("%s", window=True)' % window
    cmds.button(label='Close', command=closeCmd)

    cmds.showWindow(window)


def dorandomize_func(num_dups, min_x, max_x, min_y, max_y, min_z, max_z):
    numdups = cmds.intField(num_dups, query=True, value=True)

    minx = cmds.intField(min_x, query=True, value=True)
    maxx = cmds.intField(max_x, query=True, value=True)

    miny = cmds.intField(min_y, query=True, value=True)
    maxy = cmds.intField(max_y, query=True, value=True)

    minz = cmds.intField(min_z, query=True, value=True)
    maxz = cmds.intField(max_z, query=True, value=True)

    ObjectRandomizer.objectRand(numdups, minx, maxx, miny, maxy, minz, maxz)


createObjectRandWin()