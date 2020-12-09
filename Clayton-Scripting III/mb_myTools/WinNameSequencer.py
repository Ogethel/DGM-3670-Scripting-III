import maya.cmds as cmds
import NameSequencer


class NameSequencerUI():
    def __init__(self):
        self.my_window = 'mb_NameSequencerWindow'


    def createRenamerWin(self):
        self.delete()

        self.my_window = cmds.window(self.my_window, title='Name Sequencer Tool', widthHeight=(200, 300))
        cmds.columnLayout(columnAttach=('both', 5), rowSpacing=5, adjustableColumn=True)

        cmds.text(label='Input String')
        self.str_to_change = cmds.textField()

        cmds.textField(self.str_to_change, edit=True)

        def click(value):
            self.dorename_func(self.str_to_change)

        cmds.button(label='Rename String!', command=click)

        closeCmd = 'cmds.deleteUI("%s", window=True)' % self.my_window
        cmds.button(label='Close', command=closeCmd)

        cmds.showWindow(self.my_window)


    def dorename_func(self):
        self.str_to_replace = cmds.textField(self.str_to_change, query=True, text=True)

        NameSequencer.rename_func(self.str_to_replace)

    def delete(self):
        if cmds.window(self.my_window, exists=True):
            cmds.deleteUI(self.my_window)


NameSequencerUI.createRenamerWin()