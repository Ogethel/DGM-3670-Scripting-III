

polySphere -r 1 -sx 20 -sy 20 -ax 0 1 0 -cuv 2 -ch 1;
// Result: pSphere1 polySphere1 // 

polySphere -r 1 -sx 20 -sy 20 -ax 0 1 0 -cuv 2 -ch 1;
// Result: pSphere2 polySphere2 // 
setAttr "pSphere2.translateY" 1;
setAttr "pSphere2.scaleZ" .75;
setAttr "pSphere2.scaleX" .75;
setAttr "pSphere2.scaleY" .75;

polySphere -r 1 -sx 20 -sy 20 -ax 0 1 0 -cuv 2 -ch 1;
// Result: pSphere3 polySphere3 // 
setAttr "pSphere3.translateY" 1.8;
setAttr "pSphere3.scaleZ" .5;
setAttr "pSphere3.scaleX" .5;
setAttr "pSphere3.scaleY" .5;

polyCone -r 1 -h 2 -sx 20 -sy 1 -sz 0 -ax 0 1 0 -rcp 0 -cuv 3 -ch 1;
// Result: pCone1 polyCone1 // 
setAttr "pCone1.translateY" 1.8;
setAttr "pCone1.rotateX" 90;
scale -r 0.283197 0.283197 0.283197 ;
scale -r 1 3.147292 1 ;
move -r -os -wd 0 0.551052 0 ;
scale -r 0.992592 0.992592 0.992592 ;
scale -r 0.358159 0.358159 0.358159 ;

polySphere -r 1 -sx 20 -sy 20 -ax 0 1 0 -cuv 2 -ch 1;
// Result: pSphere4 polySphere4 // 
scale -r 1 1 0.454651 ;
scale -r 0.110358 0.110358 0.110358 ;
setAttr "pSphere5.translateY" 1.9;
move -r -os -wd 0 0 0.441719 ;
move -r -os -wd -0.145623 0 0 ;
rotate -r -os -fo 0 -13.841067 0 ;

