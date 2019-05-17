#-*- coding: utf-8 -*-
import math

class entityTNT(object):
  def __init__(self, x, y, z):
    self.setpos(x, y, z)

  def setpos(self, x, y, z):
    self.x = float(x)
    self.y = float(y)
    self.z = float(z)

  def getExplodeEntityMomentum(self, entity, d14):
    if abs(self.x - entity.x) <= 9 and abs(self.y - entity.y) <= 9 and abs(self.z - entity.z) <= 9:
      d5 = float(entity.x - self.x)
      d7 = float(entity.y + entity.getEyeHeight() - self.y)
      d8 = float(entity.y - self.y)
      d9 = float(entity.z - self.z)
      d13 = float(math.sqrt(d5 * d5 + d7 * d7 + d9 * d9))
      d12 = float(math.sqrt(d5 * d5 + d8 * d8 + d9 * d9)) / 8
      
      if d12 <= 1:
        if d13 != float(0):
          d5 = d5 / d13
          d7 = d7 / d13
          d9 = d9 / d13
          d10 = (1 - d12) * d14
          
          return(d5 * d10, d7 * d10, d9 * d10)
    else:
      return (0, 0, 0)