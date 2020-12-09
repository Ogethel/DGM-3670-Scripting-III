import maya.cmds as cmds
# Exercise
#
# Use Python to script a tool that renames the current selections into sequential order based on a specified input.
#
# Create a function that requires an argument string in the format "Name_##_NodeType" that will be used to specify the
# naming scheme. For example, the argument for a leg joint chain might be named "Leg_##_Jnt".
# The script will look for the "#" characters and replace them with the next number in a sequence.
# The number of "#" characters will also determine where number padding is needed, meaning the inserted number must be
# at least as many digits as there are "#" characters. For example, if two "##" characters were input, then the
# resultant number output must be at least 2 digits. Numbers that are too small are to be preceded by a zero
# (i.e. "Leg_##_Jnt" would begin converting to "Leg_01_Jnt", "Leg_02_Jnt", ... , "Leg_09_Jnt", "Leg_10_Jnt", etc.
# "Leg_####_Jnt" would convert to "Leg_0001_Jnt", etc.
#
# Objectives
#
#     Learn about string formatting and methods within Python, such as partition, rpartition, replace, and zfill.
#     Practice using functions.
# ls command will keep the order that you selected objects in.

# .count() go through a string and find all the instances of the that in a string and return a number
# .split() puts each set of consecutive strings into a list
'apple ' * 5

input_string = 'L_#_Arm_####_Jnt'

num_of_chars = input_string.count('#')

# print num_of_chars

# string_parts = input_string.partition('#####')
string_parts = input_string.partition('#' * num_of_chars)

# print string_parts

if string_parts[1]:
    print 'Characters are sequential.'
else:
    print 'Characters are not sequential.'
    cmds.error('Characters are not sequential. Input another string')


'L_#_Arm_####_Jnt'.count('#')

'L_#_Arm_####_Jnt'.partition("#")

sels = cmds.ls(sl=True)
all_names = []
# Local count
# Global


def rename_func(str_to_replace):
    cur_sels = cmds.ls(sl=True)

    start_string = str_to_replace
    num_padding = start_string.count('#')

    seq_num = 1

    for s in cur_sels:
        str_sections = start_string.partition('#' * num_padding)
        if str_sections[1]:
            print
            'Characters are all sequential'
            temp_num = seq_num
            changed_string = start_string.replace('#' * num_padding, ('0' * (num_padding - 1) + str(temp_num)))
            cmds.rename(s, changed_string)
            seq_num = seq_num + 1
            print
            changed_string
            else:
            print
            'Characters are not sequential, please enter another string'

    return changed_string


rename_func('L_Arm_##_joint')


# Bread crumbs from Clayton



