import maya.cmds as cmds
import random

# Class Examples from November 5th, 2020

my_string = 'le#g_##_Jnt'
('Leg_', '#', '_Jnt')

print(my_string.rpartition('#'))

help(zfill)

# Class Examples from October 29th, 2020

# Assignment: Redo the random generator in python

# for incrementer in sequence


random.randrange(-3.3,6.1)
random.random()

#  Functions  #

def add(value1=3, value2=5):
    sum = 0
    sum = value1 + value2
    return sum

add(5,4)
add('hello', str(3))  # Necessary for recasting variables
add(value2=3)  # Will change the second value only

# Arguments that are keyword dependant must be at the beginning of the function

def sub(val1, val2=5, val3=10):
    sub=0
    sub = val1 - val2 - val3
    return sub
sub(25)
# While loop example
num = 0
while (num < 10):
    print num
    num += 1

# Function long Version
duplicates = 3

for value in range(len(cmds.ls(sl=True))): # This does everything that the code under Long Version with nested loops
    print value

# Function long version
sels = cmds.ls(sl=True)

len(sels) # Returns length
list_length = len(sels)
for value in range(len(list_length)):
    print value
#

for value in 'My string':
    print value

range(5)

for value in sels:
    print value

for value in [1,2,3,4,5,6]:
    print value
    print value**2

# Basic logic

my_number = 10

if (my_number == 10):
    print "Wow, it's 10"
    my_number = 9
elif (my_number == 9):
    print "I made it to 9"
    my_number = 13
elif (my_number <0):
    print "Stop being so negative"
    my_number *= -1


else:
    print "That's not right"

# print "I'm through it!"


# Math Operations
# + : addition
# - : Subtraction
# * : Multiplication
# / : Division
# % : Modulus (Returns the remainder)
# ** : Exponent (i.e. 3**2 the same as 3^2)
# // : Floor division (-11/3 = -4)

# Comparison Operators
# == : equal to
# != : Not equal to
# <> : not equal to
# > : Greater than
# < : Less than
# >= : greater than or equal to
# <= : less than or equal to

# Assignment Operators
# = : assign value on the right to the operand on the left
# += : Adds value on the right to the operand of the left
# -= : Subtracts value on the right to the operand on the left
# *= : Multiplies ""
# /= : Divides ""
# **= : Exponents ""
# //= : floor divide ""

# Logical Operators
# and  : and
# or   : or
# not  : not

# Identity Operators
# is     : true if operands are the same object (3 is 3)
# is not : true if operands are not the same object
#
# 3 is 3
# my_string = 'hello'
# 'hello' is my_string
#
# Membership Operators
# in : checks if operand on the left is in operant on the right (i.e. 3 in [1,2,3])
# not in : checks if operand on the left is not in operand on the right
#
# 2 in [1,2,3,4,5,6]
# 3 not in [1,2,3]


# Class Examples from October 27th, 2020

sel = "Ball_Geo"
names = 'Clayton is "25" years old' # assigning a string
value = 13
my_list = ['Bill', 'Bob', 'Mark'] # Assigning a list
my_tuple = ('Steve', 'Stan', 'Sally') # Assigning a Tuple
my_dict = {"Clayton": 25, "Brandon": 24} # assigning a dictionary

print value
print my_list[2]
print my_tuple[0]
print my_dict["Brandon"]

my_list[1] = "Barbie"
# my_tuple[1] = "Barbie" does not work because the data type is immutable
my_dict['Timmy'] = 15

print names[5]
print names[-5] # Negative numbers work from the end of the list to the beginning
print names[-3:-1]
print names[-3:] # This will return up to the end of the string
print names[:] # Returns a copy of the string

sel[:-3] + "Ctrl" # This is a useful addition because we can rename variables with in scripts, like within rigging

# Class on October 20th and 22nd, 2020

# cmds.polySphere(name='Ball_Geo', subdivisionsHeight=20, subdivisionsAxis=32)
# print(cmds.polySphere('Ball_Geo', q=True, subdivisionsHeight=True))

cmds.polySphere(radius=1,
                subdivisionsX=20,
                subdivisionsY=20,
                axis=[0,1,0],
                createUVs=2,
                constructionHistory=1)
cmds.move(0, 4, 0, r=True, os=True, wd=True)
cmds.scale(3, 3, 3, r=True)
