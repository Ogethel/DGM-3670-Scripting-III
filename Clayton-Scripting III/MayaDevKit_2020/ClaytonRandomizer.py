import maya.cmds as cmds
import random

# Define a Function


def random_placement_generator(num_of_duplicates, minX, maxX, minY, maxY, minZ, maxZ):
    '''
    Duplicates selected objects and places randomly throughout the scene based on range

    Args:
        :param num_of_duplicates:
        :param minX:
        :param maxX:
        :param minY:
        :param maxY:
        :param minZ:
        :param maxZ:
        :return:
    '''
    sels = cmds.ls(sl=True)
    all_dups =[]

    for s in sels:  # s == 'ball_geo' in the first iteration
        for n in range(num_of_duplicates):

            dup = cmds.duplicate(s, rr=True)[0]  # ['ball_geo1']
            pos_x = random.uniform(minX, maxX)
            pos_y = random.uniform(minY, maxY)
            pos_z = random.uniform(minZ, maxZ)

            cmds.xform(dup, worldSpace=True, translation=[pos_x, pos_y, pos_z])  # xform moves objects relative to world 0,0,0, move will move relative to the object position
            all_dups.append(dup)

    cmds.select(all_dups, replace=True)
    return all_dups



# get current selection and loop through each item
# for each item:
#     duplicate the item
#     gereate random numbers between
#     move the duplicate to the random location
#     store all the duplicates into a list
#
# select all duplicates
# return all duplicates