import maya.cmds as cmds
import ObjectRandomizer


class RandomizerUI():
    def __init__(self):
        self.my_window = 'MB-Randomize Objects'

    def createObjectRandWin(self):
        self.my_window = cmds.window(title="MB-Randomize Objects", widthHeight=(300, 400))
        self.col_layout = cmds.columnLayout(columnAttach=('both', 5), rowSpacing=5, adjustableColumn=True)

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

        cmds.button(parent=self.col_layout, label='Randomize Objects!', c=lambda *x: self.dorandomize_func(num_dups, min_x, max_x, min_y, max_y, min_z, max_z))

        close_cmd = 'cmds.deleteUI("%s", window=True)' % self.my_window
        cmds.button(label='Close', command=close_cmd)

        cmds.showWindow(self.my_window)

    def dorandomize_func(self, num_dups, min_x, max_x, min_y, max_y, min_z, max_z):
        numdups = cmds.intField(num_dups, query=True, value=True)

        minx = cmds.intField(min_x, query=True, value=True)
        maxx = cmds.intField(max_x, query=True, value=True)

        miny = cmds.intField(min_y, query=True, value=True)
        maxy = cmds.intField(max_y, query=True, value=True)

        minz = cmds.intField(min_z, query=True, value=True)
        maxz = cmds.intField(max_z, query=True, value=True)

        ObjectRandomizer.objectRand(numdups, minx, maxx, miny, maxy, minz, maxz)


