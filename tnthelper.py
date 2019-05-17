#-*- coding: utf-8 -*-
import sys
from lib.entityTNT import entityTNT
from lib.entityPearl import entityPearl


print('input pearl x:')
px = float(input())
print('input pearl y:')
py = float(input())
print('input pearl z:')
pz = float(input())
pearl = entityPearl(px, py, pz)

print('input tnt x:')
tx = float(input())
print('input tnt y:')
ty = float(input())
print('input tnt z:')
tz = float(input())
print('input tnt count:')
tc = int(input())
tnt = entityTNT(tx, ty, tz)

while True:
  try:
    print('input d14')
    d14 = input()
    for momentum in tnt.getExplodeEntityMomentum(pearl, d14):
      print(tc * momentum)
  except KeyboardInterrupt:
    sys.exit(0)

