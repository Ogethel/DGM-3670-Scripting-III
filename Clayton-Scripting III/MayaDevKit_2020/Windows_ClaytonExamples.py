import maya.cmds as cmds

class RenamerUI():
    def __init__(self):
        self.my_window = 'clCoolToolWindow'

    def create(self):
        self.delete()

        my_window = cmds.window(my_window, title='Super Cool Tool Window', widthHeight=(200,200))

        col_layout = cmds.columnLayout(parent=my_window, adjustableColumn=True)

        name_field = cmds.textField(parent=col_layout, placeholderText='Name of new object...')

        cmds.button(parent=col_layout, label='Sphere', c='createSphere("Ball")')
        cmds.button(parent=col_layout, label='Cube', c='cmds.polyCube()')
        cmds.button(parent=col_layout, label='Torus', c='cmds.polyTorus()')
        cmds.button(parent=col_layout, label='Print field', c='print cmds.textField(name_field, q=True, text=True)')

        cmds.showWindow(self.my_window)

        def createSphere(self, name)
            print name


# Separate Test

class StudentInfo():
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade


    def print_student_info(self):
        print 'Student Name:', self.name, 'Grade', self.grade

student1 = StudentInfo('Clayton', 'F--')
student2 = StudentInfo('Brandon', 'A++')

student1.print_student_info()
student2.print_student_info()

# class TestClass():
#     def __init__(self):
#         self.name = 'Michael'
#         self.grade = 'F--'
#         print "I'm Alive"
#
#     def print_something(self, arg1, arg2):
#         print 'Something', arg1, arg2
#
# my_instance = TestClass()
# print my_instance
# my_instance.print_something('Nothing', 'Other Thing')
# print my_instance.name
# pritn my_instance.grade
