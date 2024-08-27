#seek() tell() and ohter functions

#1 - seek() method it is used to switch the pointer according the bytes. 

#2 - tell() this method is used to find the postion of the current pointer.

#example -

'''with open ("Python_Revision_challenge\hello.txt", "r") as f:
    #print(type(f)) #returns the byte format
    f.seek(10) #switches the pointer to the 10 th postion 


    print(f.tell()) # tell gives the postion of the pointer
    data = f.read(5) # it only reads the 5 characters starting form the seek positon
    print(data)
'''


# truncate() this function is used to specify the size of the file to return or print.
'''

with open ("Python_Revision_challenge\hello.txt", "w") as f:
    f.write("hello world")
    f.truncate(10) # it prints only specified number of the characters

    with open("Python_Revision_challenge\hello.txt", "r") as f:
        print(f.read()) #it prints specified byte size by truncate function 
'''

#############################################################################
#Lambda function - it is the short form of making the function in the form of variable instead of using the def function.
#anonymus function 
#[eg. double = lambda x:x*2] #used for passing as argument , used to write oneliner fuctions.
#does not have any name as in def function 

#example #1 -

'''#Traditional function 
def double(x):
    print(x*2)'''

#lambda function  1
double = lambda x:x*2 #it is oneliner and compact and does not have any name.

#print(double(2))

# ex 2
cube = lambda x:x*x*x
#print(cube(2))

'''#ex3 (multiple input)
average = lambda x,y,z: (x+y+z)/3
print(average(3,2,1))'''

#ex4 lambda function with the 'def'

'''def appl(fx, value): #we can use any lambda function at the place of fx
    return 6 + fx(value)
print(appl(cube,2)) #lambda function cube
print(appl(cube,3)) 
print(appl(lambda x:(x*x*x)/3, 2)) #the value of x here is 2 .'''


###########################################################################################

#MAP,FILETER AND REDUCE FUNCTONS - 

#MAP - FUNCTION THAT CAN BE APPLIED TO EACH ELEMENT IN THE ITERABLE AGRUMENT LIKE LIST AND TUPLE

#EXAMPLE 

def cube(x):
    return x*x*x

print(cube(2))

l = [1,2,3,4,5,6] #convert entire list  to a cube list

#traditinal method 
l2 = []
for i in l:
    l2.append(cube(i))
print(l2)

#using map function
l3 = list(map((cube),(l))) #it maps the 'cube' function to each element of the list 'l'.
print(l3)

##################

#filter - filter function is used to filter elements which qualifies certain set criteria'

#example 1

'''def fileter_function(a):
    return a>2 #returns the elements in list which are greater than 2
l1 = list(filter(fileter_function,l))
l1 = list(filter(lambda a: a > 2, l)) #filters the elements which are greater than 2
print(l1) 
'''

########################################

#Reduce -this function is used for reducing it returns the single value 
#needed to be imported from "function tools".
#applied to function in sequence and returns a single value as part of the functions

'''
from functools import reduce

numbers = [1,2,3,4,5,6,7,8,9]

def mysum(x,y):
    return x+y


sum = reduce(mysum,numbers) #it gives final result rather than giving the multiple results
print(sum)'''


##########################################################
#'is' & '==' 
#'is' compares exact location of object in memory
#'=='comapres value of the object


#example (is)

a =["Ganesh"]
b =["Ganesh"]
c = a

print(a is b)#false ,  #compare 'location' of obj in memory 
print(a is "Ganesh") #false , compares obj type with value
print(a == b)#true  compares 'value' of the obj in memory , here both are having same value
print(a == ["Ganesh"])#true
print(c is a)#true