import maya.cmds as cmds


class ToolboxUI():
    def __init__(self):
        self.my_window = 'mb_mytools_ui'

    def create(self):
        self.delete()

        self.my_window = cmds.window(self.my_window, title='mb_mytools_ui', widthHeight=(200, 200))
        self.col_layout = cmds.columnLayout(parent=self.my_window, adjustableColumn=True)

        cmds.button(parent=self.col_layout, label='Name Sequencer UI', c=lambda *x: self.call_name_sequencerUI())
        cmds.button(parent=self.col_layout, label='Object Randomizer UI', c=lambda *x: self.call_object_randomizer())
        cmds.button(parent=self.col_layout,
                    label='Freeze Transforms & Delete History',
                    c=lambda *x: self.call_freeze_delete())
        cmds.button(parent=self.col_layout, label='Parent Group', c=lambda *x: self.call_parent_group())
        cmds.button(parent=self.col_layout, label='Parent Constrain', c=lambda *x: self.call_parent_constrain())
        cmds.button(parent=self.col_layout, label='Show Attributes', c=lambda *x: self.call_show_atter())

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

    def call_freeze_delete(self):
        import win_history_delete
        reload(win_history_delete)
        cfd_instance = win_history_delete.HistoryTransManager()
        cfd_instance.create_history_manager()

    def call_parent_group(self):
        import parent_group
        reload(parent_group)
        pg_instance = parent_group.parent_group_sel()
        pg_instance()

    def call_parent_constrain(self):
        import parent_scale_constrain
        reload(parent_scale_constrain)
        psc_instance = parent_scale_constrain.parent_constrain()
        psc_instance()

    def call_show_atter(self):
        import toggle_localrot_axes
        reload(toggle_localrot_axes)
        tla_instance = toggle_localrot_axes.toggle_attr()
        tla_instance()





# tb = ToolboxUI()
# tb.create()