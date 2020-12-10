#Polevector position calculation. Creates a locator at a correct position by NH
import maya.cmds as mc
import maya.OpenMaya as OM

sel = mc.ls(sl=True)

start = mc.xform(sel[0], q=1, ws=1, t=1)
mid = mc.xform(sel[1], q=1, ws=1, t=1)
end = mc.xform(sel[2], q=1, ws=1, t=1)

startV = OM.MVector(start[0], start[1], start[2])
midV = OM.MVector(mid[0], mid[1], mid[2])
endV = OM.MVector(end[0], end[1], end[2])

startEnd = endV - startV
startMid = midV - startV

dotP = startMid * startEnd

proj = float(dotP) / float(startEnd.length())

startEndN = startEnd.normal()

projV = startEndN * proj

arrowV = startMid - projV
arrowV *= 5 # Descides the distance.
finalV = arrowV + midV

# creates a locator and moves it to the final vector position
loc = mc.spaceLocator()[0]
mc.xform(loc, ws=1, t= (finalV.x, finalV.y, finalV.z))

