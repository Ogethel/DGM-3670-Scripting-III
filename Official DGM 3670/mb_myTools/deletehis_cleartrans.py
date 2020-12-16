import maya.cmds as cmds


def Clean_Objects():
    sel_objects = cmds.ls(selection=True)

    for i in sel_objects:
        cmds.delete(i, constructionHistory=True)
        cmds.makeIdentity(i, apply=True, t=1, r=1, s=1, n=0)


def Delete_History():
    sel_objects = cmds.ls(selection=True)

    for i in sel_objects:
        cmds.delete(i, constructionHistory=True)


def Freeze_Transform():
    sel_objects = cmds.ls(selection=True)

    for i in sel_objects:
        cmds.makeIdentity(i, apply=True, t=1, r=1, s=1, n=0)



# Example Script:
'''
rigSelection = cmds.ls(selection=True)

for items in rigSelection:


    cmds.listRelatives(shapes=True)


    cleanDuplicate = cmds.duplicate(rigSelection, name= str(items) + str(cleanGeo))


    conDuplicate = cmds.duplicate(rigSelection, name= str(items) + str(conGeo))


    for cleaner in items:

        cmds.delete(constructionHistory=True)

        cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)

    items = cleanDuplicate + conDuplicate  # where cleanDuplicate/conDuplicate are []
    for cleaner in items:
        cmds.delete(cleaner, constructionHistory=True)
        cmds.makeIdentity(cleaner, apply=True, t=1, r=1, s=1, n=0)
'''
