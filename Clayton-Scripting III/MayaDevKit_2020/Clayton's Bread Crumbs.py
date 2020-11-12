# Bread crumbs from Clayton
import maya.cmds as cmds

input_string = 'L_#_Arm_####_Jnt'

num_of_chars = input_string.count('#')

string_parts = input_string.partition('#' * num_of_chars) # ['L_Leg_', #####', '_Jnt']
                                                          # ['L_L#eg ##### Jnt', '', '']

# zfill will allow for auto input padding

if string_parts[1]:
    print 'Characters are sequential.'
else:
    print 'Characters are not sequential.'
    cmds.error('Characters are not sequential. Input another string')


'L_#_Arm_####_Jnt'.count('#')

'L_#_Arm_####_Jnt'.partition("#")