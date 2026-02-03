import textwrap
import string
import sys
import array
import random
width = 150

def discuss_whatever2():
    writing = "this is a lot of text this is a lot of text this is a lot of text" \
    "this is a lot of text this is a lot of text this is a lot of text this is a lot " \
    "of text this is a lot of text this is a lot of text this is a lot of text this is " \
    "a lot of text"
    print(textwrap.fill(writing,width))

#def wrap_text(writing, width):
 #   return textwrap.fill(writing, width)

discuss_whatever2()