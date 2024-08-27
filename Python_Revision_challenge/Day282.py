#Magic / Dunder Methods in python 
'''these are special methods that you can define in your classes and when included they give
you a powerful manipulation objects and their behaviour. They are also known as "dunders" 
from 'double' underscore surrounding. They are used to perform special methods such as addtion
substraction and comparison operator as well as some more advanced technique'''


#1[__init__ method]- 
'''it is basically a special method that is automatically included when we create new instance of class.
This method is responsiblefor setting up the objects initial state and its also called as "constructor"
'''

#2[__str__ and __repr__ methods]-
'''the __str__ and __repr__ methods are both used to convert an object a string representation
that is converted an object of a string representation that 'str' method is used when you want to 
print an object while the 'repr' is used when you want to get the string representation of an
object that can be used to recreate an object'''

#3[__len__ method]- 
'''The '__len__'  method is used to get the length of the object this is useful method when you want 
to be able to find the size of a data structure such as list for dictionary'''

#4 [__call__ metod]-
'''The '__call__' method is used to make the object callable means you can pars it as a parameter 
to a function and it can be executed when ever called '''


#example 1 -

class Employee:
    def __init__(self,name):
        self.name = name

    def __len__(self): #used to get full length of an object
        i =0 
        for c in self.name:
            i = i+1
        return i
    
    def __str__(self): #when you want to print an object
        return (f"The name of the employee is {self.name}str")
    
    def __repr__(self): #the 'repr' is used when you want to get the string representation of an object that can be used to recreate an object
        return (f"the name2 of the employee is {self.name}")
    
    def __call__(self):#it makes object callable from anywhere
        print("hey i am good")


        


