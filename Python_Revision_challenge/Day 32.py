#Time module in python - 
'''The timemodule in python provides a set of the functions to work with the 
time related operations such as time keeeping. formatring and time conversation
this a part of python installation making a covinient and essential tool for 
wide range of applications'''


#time.time() -
'''the time.time() function return the crrent time as floating point number
representing the number of seconds since epoch(the time point when the moudle
was initialized) the returned value is based on the computers system clock 
and is affected by the time adjustments made by the os'''

#time.strftime() - 

'''The time.strftime() function fromat is a time value as a 'string' based on 
a specific fromat this function is perticularly usrful for formatting dates and times
in human -readable format such as for display in a out a long tie or a report
(which is in year,month,day  & hour,minuit,second format)'''
  
#example 1 -

import time

#print(time.time()) #time in seconds since the epoch (epoch - when module is initialized')

formattedtime = time.strftime("%y-%m-%d %H:%M:%S") #date format should small and time should ne cap
#print(formattedtime)

'''IT IS used to format time objects into readable strings.
To use it effectively, you need to pass a format string that specifies 
 how you want the time to be formatted. '''

def usingwhile():
    i = 0
    while i < 1500:
        i = i+1
        print(i)

def usingfor():
    for i in range (5000):
        print(i)


init = time.time() #current tiem in seconds

#usingwhile() #function to print numbers till 1500

t1 = (time.time() - init)
init = time.time()

#usingfor()

#print(time.time() - init)
#print(t1) #return time taken by the loops


##################################################################

#EXAMPLE 2

#time.sleep()- this function is used to wait the program execution for desired
#time.


print(5) 

time.sleep(5) #used to hold program execution
print("this line is printed after 5 second hold")

################################################################
#EXAMPLE 3

'''while True:
    #print(time.localtime()) #current time in seconds 
    #formatted_time = time.strftime("%y-%m-%d %H:%M:%S")
    seconds = time.strftime("%M:%S")
    print(seconds)
    time.sleep(5)
    print(seconds)

    #print(formatted_time)'''

######################################################################################################

#walrus operator in python - 
'''The walrus operator is a new addtion in python 3.8 and allows you to 
assign a value to a variable within a expression.This can be useful when 
you need to use a value multiple times in a loop but dont wnat to repeat
the calculations.

it is represeted by ':=' syntax and could be used a variety of contexts including
while loop and statement'''


#Example : 

a = "True"
print(a:="false")#value assgined



