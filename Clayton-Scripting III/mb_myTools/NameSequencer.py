import maya.cmds as cmds


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