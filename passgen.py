# passgen.py
# Created by Doug Leidgen, June 2021
# This program can be freely distributed

import random
import string
import sys
try:
    import pyperclip
except:
    print("Error: pyperclip not found.")
    print("Install the module with pip in order to copy the password to your clipboard")
    print("Usage:  pip3 install pyperclip")

print("Your password will be printed below\n")

#This variable sets the length of the password
length = 16

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symb = string.punctuation

allp = lower + upper + num + symb
temp = random.sample(allp, length)

password = "".join(temp)

print(password)
print('\n')

try:
    pyperclip.copy(password)
    print("Your password has been copied to your system clipboard")
except:
    print("Password not copied to clipboard")

del password
sys.exit()
