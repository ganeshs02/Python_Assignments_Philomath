
#walrus operator in python - 
'''The walrus operator is a new addtion in python 3.8 and allows you to 
assign a value to a variable within a expression.This can be useful when 
you need to use a value multiple times in a loop but dont wnat to repeat
the calculations.

it is represeted by ':=' syntax and could be used a variety of contexts including
while loop and statement'''


#Example 1: 

a = "True"
print(a:="false")#value assgined


#Example 2:

numbers = [1,2,3,4,5,6,7]

while(n := len(numbers))>0: #here we assigned len value to 'n' variable
    print(numbers.pop())


#Example 3:

happy = "false"
#print(happy)

#print(happy:= "true")


#exmaple 4

foods = list()
'''
while (food:= input("what would you like to eat?:")) != "quit": #loop will continue to execute till "quit".
    foods.append(food)
    print(foods)
'''

#exmaple 4 :
#with walrus operator - increases readablity
# 
#  
'''icecreams = list()

print(icecreams)
while(icecreams:=input("what whould you like to eat?:"))!="quit":
    foods.append(icecreams)
    print(icecreams)'''

#without walrus operator
'''
foods = list()

while True:
    food = input("enter what would you like to eat:?")
    if foods == "quit":
        break
    foods.appned(food)


'''

#######################################################################################

# shutil - "shell utility module" (bulilt in function) (file directories autiomation)

'''Shutil module in a python module that provides a higher level interface for working 
with the files and directories. The name 'shutil is a short for 'shell utility' it provide
convinient and efficient way to automate tasks that are commonly performed on file and directories 
in this .'''


import shutil
import os
import orgparse
###################
 #1 shutil.copy(src,destination) 
'''This function copies the file located at source to a new location specified by dist . if
 the destination location specified by dest. if the desctination location already exits
 the original file will be overwritten'''

file_path = r"C:\Users\Ganseh\Desktop\Python Assignments\Python_Revision_challenge\PDFS\merged-pdf.pdf"
file_dst =r"C:\Users\Ganseh\Desktop\Python Assignments\Python_Revision_challenge\PDFS\hihi.pdf"

path = os.path.normpath(file_path) #to get the path as an input without usig raw string.
print(path)

shutil.copy(file_path,file_dst) #copies file from 'file_path' to 'file_dst' 


##########################

#2 shutil.copy2(src,dst) - 
'''This function is similar to 'copy' but it also preserves more 'metadata' about that original 
file such as the timestamp'''

shutil.copy2(file_path,"merg") #it copies the meta data also


#shutil.copytree(src,dst) - 
'''This function recrusively copies the directory located at 'src' to a new location by 'dst' 
if the destination location already exists the original (only directories)'''

dir_path = os.path.normpath(input("enter the directory file path:"))



shutil.copytree(dir_path,"books") #it copies the directory and it s contents

#########################

#Shutil.move(src,dst) 
'''This function moves the file located at the 'src' to a new location specified by 'dst' 
this function is quivalent to renaming file  and moving the files in most cases '''

shutil.move("merg",r"Python_Revision_challenge\PDFS") #moves the file form location to destination

shutil.move("hihi.pdf","dj.pdf") #renames the file also

shutil.move("Python_Revision_challenge\PDFS","bookpdfs") #renames the files and directories

###########################

#shutil.rmtree(path) - 
'''This function recursively deletes the directory located at the path along with all
of its contents this function is similar to using the 'r -rf' command in linux /shell .'''

shutil.rmtree("books") #removes the dirs
os.remove("filename")  #removes the files


