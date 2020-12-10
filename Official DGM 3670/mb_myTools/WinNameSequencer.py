import maya.cmds as cmds
import NameSequencer


class NameSequencerUI():
    def __init__(self):
        self.my_window = 'Name Sequencer Tool'

    def createRenamerWin(self):
        self.delete()

        self.my_window = cmds.window(self.my_window, title='Name Sequencer Tool', widthHeight=(200, 300))
        self.col_layout = cmds.columnLayout(columnAttach=('both', 5), rowSpacing=5, adjustableColumn=True)

        cmds.text(label='Input String')
        str_to_change = cmds.textField()
        cmds.textField(str_to_change, edit=True)

        cmds.button(parent=self.col_layout, label='Rename String!', c=lambda *x: self.dorename_func(str_to_change))

        closeCmd = 'cmds.deleteUI("%s", window=True)' % self.my_window
        cmds.button(parent=self.col_layout, label='Close', command=closeCmd)

        cmds.showWindow(self.my_window)

    def dorename_func(self, input_string):
        new_str_to_change = input_string
        str_to_replace = cmds.textField(new_str_to_change, query=True, text=True)
        NameSequencer.rename_func(str_to_replace)

    def delete(self):
        if cmds.window(self.my_window, exists=True):
            cmds.deleteUI(self.my_window)



