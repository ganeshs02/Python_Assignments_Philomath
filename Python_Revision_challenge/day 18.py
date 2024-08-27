# (if name == "__main__") in the python.
#used to run script run directly or its running as a import of being in many module.
# main function contain the code that should run while the script is run directly.
#"__name__" variable is equal to "__main__" is main function.


#example 1

'''import example


example.name()'''

 #to run script directly

'''Basically if"__name__ = "__main__" works as an check to stop the execution of other files except files  in main.'''
#################################################################################################################################

''' OS MODULE IN PYTHON (AUTOMATE TASKS) - through this module we can automate operating system tasks'''
# This module has multiple functions which can do many tasks susch as (mkdir,delete,list dir etc and many more).

#example 1(main directly) #to create directories automatically

import os


'''
# Ensure the 'data' directory exists before creating subdirectories
os.makedirs('data', exist_ok=True)

# Create 5 directories named 'day 1', 'day 2', etc.
for i in range(5):
    os.mkdir(f"data/day {i+1}")'''



#example 2 - Reanaming directories automatically(first give source and then destination)
'''
import os 

for i in range(0, 100):
    os.rename(f"data/day {i+1}", f"data/name {i+1}") # it changes all the file from tutorial to challenge'''

#example 3 - listing directories

'''import os

folders = os.listdir("data")

print(folders)

for folder in folders:
    print(folder)
    print(os.listdir(f"data/{folder}"))'''






