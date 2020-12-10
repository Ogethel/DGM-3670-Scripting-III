import maya.cmds as cmds


class Toolbox_UI():
    def __init__(self):
        self.my_window = 'mb_mytools_ui'

    def create(self):
        self.delete()

        self.my_window = cmds.window(self.my_window, title='mb_mytools_ui', widthHeight=(200, 200))
        self.col_layout = cmds.columnLayout(parent=self.my_window, adjustableColumn=True)

        cmds.button(parent=self.col_layout, label='Name Sequencer UI', c=lambda *x: self.call_name_sequencerUI())
        cmds.button(parent=self.col_layout, label='Object Randomizer UI', c=lambda *x: self.call_object_randomizer())

        cmds.showWindow(self.my_window)

    def delete(self):
        if cmds.window(self.my_window, exists=True):
            cmds.deleteUI(self.my_window)

    def call_name_sequencerUI(self):
        import WinNameSequencer
        reload(WinNameSequencer)
        name_sequencerUI_instnace = WinNameSequencer.NameSequencerUI()
        name_sequencerUI_instnace.createRenamerWin()

    def call_object_randomizer(self):
        import WinObjectRandomizer
        reload (WinObjectRandomizer)
        object_randUI_instance = WinObjectRandomizer.RandomizerUI()
        object_randUI_instance.createObjectRandWin()


# tb = Toolbox_UI()
# tb.create()