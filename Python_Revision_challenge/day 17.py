# import  - to import the predefined code and functions
# for importing perticular function use (from math import sqrt,p)
#for importing all the functions use (from math import *) but gets confused.

# AS keyword - to give a short name to a module

import math as m # given m as a short name
############

# dir function -  to print all the functions in the module

print(dir(m)) #to print all the functions in the math

###########

#example 1

result = m.sqrt(4) #function to print square root
print(result)

#exmaple 2 (import) - to permanently import any function form module

from math import pi # to import pi function

print(m.sqrt(4)) #here we used modulename.function name

print(pi) #after importing it we dont need to use 'modulename.'


# example 3 -

from math import * #to import all functions from module

#example 4 - (as keyword) #reduce the module size

import math as m # short form

result = m.sqrt(16)
print(result)


#exmaple 5 - (to print all the function in the module)

print(dir(m))


#exmaple 6 -  # to import the function created in the another file to use in this file
'''To import previously saved programs in current module'''

from example import name
name()
name()




##################################################################################################################################

