#challenge 2

#make a program which will print greetings according to timestamp.

import time
'''all_attr = dir(time)  #to get all the functions inside the package.
print(all_attr)'''


timestamp = (time.strftime('%H:%M:%S')) #to print current time
print(timestamp) 

timestamp = (time.strftime("%H")) #to print hour
print(timestamp)

timestamp = (time.strftime("%M")) #to print min
print(timestamp)

timestamp = (time.strftime("%S"))  #to print sec
print(timestamp)

##### if else condition part ###################

if int(time.strftime("%H")) >= 0 and int(time.strftime("%H")) <= 11:
    print("Hello Good Morning Sir!")

elif int(time.strftime("%H")) >= 12 and int(time.strftime("%H")) <= 17:
    print("Hello Sir Good Afternoon!😀")

elif int(time.strftime("%H")) >= 17 and int(time.strftime("%H")) <= 21:
    print("Hello sir Good Evening!😁")

elif int(time.strftime("%H"))>= 21 and int(time.strftime("%H")) <= 24:
    print("Hello sir Good Night!😴")

else:
    ("you are probably not on earth!")
