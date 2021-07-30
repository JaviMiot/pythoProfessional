"""uso de sets"""

#? Union en python se lo hace con |
set1 = {1,2,3,4,5,6,7,8}
set2 = {8,9,10,11}

setUnion = set1 | set2
print('Union sets')
print(setUnion)

#? Interseccion lo que tien en comun se hace con &
setInter = set1 & set2
print('Interseccion sets')
print(setInter)

#? diferencia se lo hace con -
setDiff1 = set1 - set2
setDiff2 = set2 - set1
print('Diff sets')
print(setDiff1)
print(setDiff2)

#? Diferencia simetrica. te quedas con los elementos
#? diferentes. Se hace con ^
setDiffSi = set1 ^ set2
setDiff2 = set2 - set1
print('Diff Simetrica sets')
print(setDiffSi)
