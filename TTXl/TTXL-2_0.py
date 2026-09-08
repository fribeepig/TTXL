#Transtextual, ver 2, complete reboot, Started: 9/8/2026

#imported utilities
import textwrap
import string
import sys
import array
import random

def start_game():
    intro = ""
    print(textwrap.fill(intro,width))


#The Stuff to make stuff work... I think, it's been a while

def pause(): #Pause and wait for user input function
    choice = input("").lower().strip()
    if choice == "":
        pass
    else:
        pass

#Start Screen
def start_screen(): #Start screena
    print("Welcome to")
    title()
    print("       by Sophie")
    print("Do you want to Start, access Settings or do you need Help?")
    choice = input("> ").lower().strip()
    if choice == "start":
        start_game() 
    elif choice == "help":
        help_screen() 
    elif choice == "settings":
        width_set()
    else:
        print("I'm sorry, I don't understand")
        print()
        start_screen()

def width_set():
    while True:
        print("The default text width is '150', after choosing a new value, an example text will be displayed.")
        value = input("Input New Value> ")
        width.pop(0)
        width.insert(0,value)
        example_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque vel aliquam urna. Fusce suscipit gravida nisi, id placerat massa imperdiet sit amet. Mauris venenatis, quam et laoreet euismod, risus augue efficitur lectus, sit amet interdum ante massa in mauris. Vivamus ut est et nisl auctor rutrum eget ut mauris. Fusce ullamcorper, dui interdum interdum ultrices, lacus magna luctus risus, eu eleifend nisl nunc a est. Morbi in ex consectetur, sagittis est sit amet, feugiat turpis. Nam quis tincidunt dui. Morbi sodales auctor mauris vitae mattis. Vivamus vitae ullamcorper erat, sit amet faucibus arcu. Integer vitae tempus urna, id egestas libero. Duis nec lacus vehicula, sollicitudin est sed, tincidunt magna. Integer tincidunt nisi id justo consectetur, a ultrices nibh hendrerit. Morbi condimentum consequat tristique. Etiam imperdiet massa sit amet justo fringilla, ut mollis nisi luctus. "
        print(textwrap.fill(example_text,width))
        pause()
        check = input("Does that look right? y/n ")
        if check == "y":
            break
        elif check == "n":
            pass
    start_screen()

#Global Variables

cursce = [start_game]
width = [150]

start_screen() #has to be the very end. All "def scene():" must occur in the code before they are reffered to?

def title():
    print("    .....                                                    .x+=:.        s                                 s                                     .. ")
    print(" .H8888888h.  ~-.                                           z`    ^%      :8                                :8                               x .d88\"  ")
    print(" 888888888888x  `>    .u    .                  u.    u.        .   <k    .88                  uL   ..      .88       x.    .                  5888R   ")
    print("X~     `?888888hx~  .d88B :@8c        u      x@88k u@88c.    .@8Ned8\"   :888ooo      .u     .@88b  @88R   :888ooo  .@88k  z88u         u      '888R   ")
    print("'      x8.^\"*88*\"  =\"8888f8888r    us888u.  ^\"8888\"\"8888\"  .@^%8888\"  -*8888888   ud8888.  '\"Y888k/\"*P  -*8888888 ~\"8888 ^8888      us888u.    888R   ")
    print(" `-:- X8888x         4888>'88\"  .@88 \"8888\"   8888  888R  x88:  `)8b.   8888    :888'8888.    Y888L       8888      8888  888R   .@88 \"8888\"   888R   ")
    print("      488888>        4888> '    9888  9888    8888  888R  8888N=*8888   8888    d888 '88%\"     8888       8888      8888  888R   9888  9888    888R   ")
    print("    .. `\"88*         4888>      9888  9888    8888  888R   %8\"    R88   8888    8888.+\"        `888N      8888      8888  888R   9888  9888    888R   ")
    print("  x88888nX\"      .  .d888L .+   9888  9888    8888  888R    @8Wou 9%   .8888Lu= 8888L       .u./\"888&    .8888Lu=   8888 ,888B . 9888  9888    888R   ")
    print(" !\"*8888888n..  :   ^\"8888*\"    9888  9888   \"*88*\" 8888\" .888888P`    ^%888*   '8888c. .+ d888\" Y888*\"  ^%888*    \"8888Y 8888\"  9888  9888   .888B .")
    print("'    \"*88888888*       \"Y\"      \"888*\"\"888\"    \"\"   'Y\"   `   ^\"F        'Y\"     \"88888%   ` \"Y   Y\"       'Y\"      `Y\"   'YP    \"888*\"\"888\"  ^*888%  ")
    print("        ^\"***\"`                  ^Y\"   ^Y'                                         \"YP'                                           ^Y\"   ^Y'     \"%    ")