#Asyncio in python  - (import Asyncio)

'''Asyncio (Asynchronous I/O) or a short in a program pattern allows high perforamance in a
concurrent and non-blocking manner in python 'async' programming is achieved through the use of 
asyncio module and asynchronous function  '''

'''
asyncio in Python is a library used to write programs that can "perform many tasks at once" without 
waiting for one task to finish before starting another. This is useful when you have tasks that 
might take some time to complete, like downloading files from the internet or reading large files
 from disk, and you don't want your program to just sit there doing nothing while it waits.'''

#asyncio helps you make better use of your time by letting multiple tasks work together efficiently!


#Example 1  - 

import asyncio
import time 





async def function1(): #asynchronous function ("async" at the start)
    await asyncio.sleep(2)
    print("this is function 1")
    return "ganesh"

async def function2():
    await asyncio.sleep(5)
    print("this is function 2")
    return "ganesh"

async def function3():
    await asyncio.sleep(2)
    print("this is function 3")
    return "ganesh"


'''async def main():
    task = asyncio.create_task(function1()) #whenever it get time it gets excuted(slow)
    await (function1())
    await (function2())
    await (function3())'''
#in this type we are not able to organize the function execution.

###################################################################################

async def main():
    task = await asyncio.gather( #it is used to run the functions parellelly (fast)
         (function1()),          #"gather function dont need async at the start!!!!"
         (function2()),
         (function3()),
    )
    print(task)

#so basically here we can organize the execution of the code. and it can run (fastly).

asyncio.run(main())

########################################################################################################################

#Excercise 11 - DRINK WATER REMINDER
'''Write a python program which returns you of drinking 
water every hour or two your program can either beep or send desktop
notification for a specific operating system.'''




