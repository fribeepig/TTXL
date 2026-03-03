import textwrap
import string
import sys
import array
import random

spot = [0,0,0]

def Go_Down():
    if spot.index(0) >> 0:
       y = spot.index(0)-1
       spot.pop(0)
       spot.insert(0,y)
    else:
       y2 = spot.index(0)-1
       spot.pop(0)
       spot.insert(0,y2)
    
print(spot)
Go_Down()
print(spot)
Go_Down()
print(spot)
Go_Down()
print(spot)
Go_Down()
print(spot)
Go_Down()