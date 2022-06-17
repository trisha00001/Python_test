from math import pi

def pl(radius):
     if type (radius) not in [int, float]:
          raise TypeError("Only numbers")
     if radius <0:
          raise ValueError("r<0")
     return pi*radius**2
