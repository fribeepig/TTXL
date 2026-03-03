import textwrap
import string
import sys
import array
import random

# @ = You
# # = Wall
# * = Points you can go to within your range
# $ = Treasure
# ^ = Basic Enemy
# % = Tougher Enemy
# & = Boss?

# width = 14

#print(textwrap.fill(Top_T,14))

#" 1 2 3 4 5 6 7  " 
#"1     #   #     " 
#"2     #   #     " 
#"3 # # #   # # # " 
#"4       @       " 
#"5 # # #   # # # " 
#"6     #   #     " 
#"7     #   #     "



Crossroads = " 1 2 3 4 5 6 7 " "1     #   #     " "2     #   #     " "3 # # #   # # # " "4       @       " "5 # # #   # # # " "6     #   #     " "7     #   #    "

BLC = "  1 2 3 4 5 6 7 " "1              " "2              " "3 # # # # #     " "4       @ #     " "5 # # #   #     " "6     #   #     " "7     #   #    "

BRC = "  1 2 3 4 5 6 7 " "1              " "2              " "3     # # # # # " "4     # @       " "5     #   # # # " "6     #   #     " "7     #   #    "

TRC = "  1 2 3 4 5 6 7 " "1     #   #    " "2     #   #    " "3     #   # # # " "4     # @       " "5     # # # # # " "6               " "7              "

TLC = "  1 2 3 4 5 6 7 " "1     #   #    " "2     #   #    " "3 # # #   #     " "4       @ #     " "5 # # # # #     " "6               " "7              "

Top_T = "  1 2 3 4 5 6 7 " "1     #   #    " "2     #   #    " "3 # # #   # # # " "4       @       " "5 # # # # # # # " "6               " "7              "

Bot_T = "  1 2 3 4 5 6 7 " "1              " "2              " "3 # # # # # # # " "4       @       " "5 # # #   # # # " "6     #   #     " "7     #   #    "

Rit_T = "  1 2 3 4 5 6 7 " "1     #   #    " "2     #   #    " "3     #   # # # " "4     # @       " "5     #   # # # " "6     #   #     " "7     #   #    "

Lef_T = "  1 2 3 4 5 6 7 " "1     #   #    " "2     #   #    " "3 # # #   #    " "4       @ #    " "5 # # #   #    " "6     #   #    " "7     #   #    "

Top_Room = "  1 2 3 4 5 6 7" "1     #   #    " "2     #   #    " "3     #   #    " "4     # @ #    " "5     #   #    " "6     # # #    " "7              "

Rit_Room = "  1 2 3 4 5 6 7" "1              " "2              " "3   # # # # # #" "4   #   @      " "5   # # # # # #" "6              " "7              "

Lef_Room = "  1 2 3 4 5 6 7" "1              " "2              " "3 # # # # # #  " "4       @   #  " "5 # # # # # #  " "6              " "7              "

Bot_Room = "  1 2 3 4 5 6 7" "1              " "2     # # #    " "3     #   #    " "4     # @ #    " "5     #   #    " "6     #   #    " "7     #   #    "

Hori_Hall = "  1 2 3 4 5 6 7" "1              " "2              " "3 # # # # # # #" "4       @      " "5 # # # # # # #" "6              " "7              "

Vert_Hall = "  1 2 3 4 5 6 7" "1     #   #    " "2     #   #    " "3     #   #    " "4     # @ #    " "5     #   #    " "6     #   #    " "7     #   #    "

Hori_Room = "  1 2 3 4 5 6 7" "1              " "2   # # # # #  " "3 #           #" "4       @      " "5 #           #" "6   # # # # #  " "7              "

Vert_Room = "  1 2 3 4 5 6 7" "1     #   #    " "2   #       #  " "3   #       #  " "4   #   @   #  " "5   #       #  " "6   #       #  " "7     #   #    "

Boss_Door_Clos = "  1 2 3 4 5 6 7" "1   #       #  " "2   # % % % #  " "3   #       #  " "4   #   @   #  " "5   #       #  " "6   #       #  " "7     #   #    "

Boss_Door_Open = "  1 2 3 4 5 6 7" "1   #       #  " "2   #       #  " "3   #       #  " "4   #   @   #  " "5   #       #  " "6   #       #  " "7     #   #    "

Treas_Room = "  1 2 3 4 5 6 7" "1   # #   # #  " "2 #           #" "3 #           #" "4      [$]     " "5 #           #" "6 #           #" "7   # #   # #  "



spot = [0,0,0]

def Go_Up():
    x = spot.index(0)+1
    spot.pop(0)
    spot.insert(0,x)

def Go_Down():
    a = spot.index(0)-1
    spot.pop(0)
    spot.insert(0,a)

def Go_Right():
    y = spot.index(1)+1
    spot.pop(1)
    spot.insert(1,y)

def Go_Left():
    b = spot.index(1)-1
    spot.pop(1)
    spot.insert(1,b)

def Go_Upstairs():
    spot.pop(0)
    spot.insert(0,0)
    spot.pop(1)
    spot.insert(1,0)
    z = spot.index(2)+1
    spot.pop(2)
    spot.insert(2,z)




