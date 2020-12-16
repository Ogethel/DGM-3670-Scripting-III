import maya.cmds as cmds
import deletehis_cleartrans


class HistoryTransManager():
    def __init__(self):
        self.my_window = 'History & Transform Manager'

    def create_history_manager(self):
        self.delete()

        self.my_window = cmds.window(self.my_window, title='History & Transform Manager', widthHeight=(200, 300))
        self.col_layout = cmds.columnLayout(columnAttach=('both', 5), rowSpacing=5, adjustableColumn=True)

        cmds.button(parent=self.col_layout, label='Delete History!', c=lambda *x: self.delete_history_only())
        cmds.button(parent=self.col_layout, label='Freeze Transforms!', c=lambda *x: self.freeze_trans_only())
        cmds.button(parent=self.col_layout, label='Clean Object!', c=lambda *x: self.clean_object())

        closeCmd = 'cmds.deleteUI("%s", window=True)' % self.my_window
        cmds.button(parent=self.col_layout, label='Close', command=closeCmd)

        cmds.showWindow(self.my_window)

    def delete_history_only(self):
        deletehis_cleartrans.Delete_History()

    def freeze_trans_only(self):
        deletehis_cleartrans.Freeze_Transform()

    def clean_object(self):
        deletehis_cleartrans.Clean_Objects()

    def delete(self):
        if cmds.window(self.my_window, exists=True):
            cmds.deleteUI(self.my_window)