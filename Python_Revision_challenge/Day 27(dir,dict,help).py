# Static methods - these are the methods which does not belong to the instance as well as class.
#static methods in python are methods that belong to a class rather than a instance of class.
# they are defined using the "@static method" decorator and do not have access to instance of class.
# they are often used to create utility functions that doesnt need access to instance data.
# static methods does not need "self" keyword.

'''
INTERVIEW QUESTION - is is necessary to pass self argument to create a method in class?

Answer - The answer is no we can use "static method 1 " without using argument which does
not need 'self' keyword argument for creating method ''' 

#Example - 
#Static methods in python 
'''
class Math:
    def __init__(self, num):
        self.num = num


    def addtonum(self,n):
        self.num = self.num + n 


    @staticmethod   #belongs to class not 
    def add (a,b):
        return a+b 


result = Math.add(1,2) #used static method without using "self"
print(result) #output : 3

a  = Math(5)
print(a.num) #output : 5
a.addtonum(6)
print(a.num) #output :5+6 =11'''


#######################################################################################################
#Instance variable and Class Variables 

'''
class variables - variables that are delivered at the class level and are shared among all the instances 
of the class they are defined outside of the an method and are usually used to store information that is 
common to all the instances of the class that have been created 
eg. classs varaible can be used to store number of instances.

Instance variables - Instance variables are the defined at the instace level and are unique to each instance 
of the class they are defied inside the init method and are usually used to store information that is specific to each
instance of the class.
eg. Instance variable can used to store name of the employee in the class that represent employee.'''

''''
class Employees:
    company_name = "NVIDIA" #these are classs variables
    company_location = "Satara" #these are classs variables
    no_of_employees = 0 

    def __init__(self, name):
        self.name  = name
        self.raise_amount = 0.02 #these are instance variales
        Employees.no_of_employees += 1
    
    def showdetails(self):
        print(f"""The name of the employees is {self.name} and the #user tripel
              raise amount in {self.company_name},{self.company_location} is {self.raise_amount} .""")
        


emp1 = Employees("Ganesh")# it will print default class variables
emp1.raise_amount = 3   
Employees.showdetails(emp1)


emp2 = Employees("Nikhill") #it will print modified class variables
emp2.raise_amount = 0.3
emp2.company_name = "AMD" #changed the class varaibles for perticualr employees 
emp2.showdetails() #or
#Employees.showdetails(emp2)

Employees.company_name = "solaris" #changed for all the employees
emp1.showdetails()'''

########################################################################################################
#CLASS METHODS -
'''class methods are the way to define custom data types tht can store data and define functions that
can be defined within a class is called as the class methods.'''

'''a class method is a type of the method that is bound to be class of the instance of the class
in other words it operates the class as a whole rather than on a specific instances of the class'''

#Cla-ss methods are defined using "@class method" decorator followed by the function is always 'cls' which
#represent the class.
''' use case  - popular alternative contructors for class'''


'''exmple - to  define class method you simply use the @classmethod as the first argument of 
the method should always be "cls" which represent the class itself '''

#exmaple syntax 

def factory_method(cls,argument1,argument2):
    return cls(argument1, argument2)

#example 1 :

class Employee:
    company = "Apple"  #class variable

    def showdetails(self):
        print(f"the name of the employee is {self.name} and the company is {self.company}")


    @classmethod
    def changecompany(cls, newcompany): #here we used 'cls' for class
        cls.company = newcompany   #here we used the class method to modify the class variable 


e1 = Employee()
e1.name = "Ganesh"
e1.showdetails() #default class variable 

e1.changecompany("manjara") #changig the class variable 
e1.showdetails()

e2 = Employee()
e2.name = "nikhil"
e2.showdetails() 
print(Employee.company) #default class variable name is also been changed after applying @classmethod decorator

#################################################################################


#dir() and __dict__() and help method :

#they make it easy for to understand how classes resolve various functions and excutes code in python

#they are built in functions that are community used to get informatio about the object dir(), dict(), help()

# 1 DIR() METHOD :-
'''The dir() function 'returns a list of all the attributes and methods including dunder methods' 
available for an object. it is a useful for discovering "what you can do with an object" '''

#example - 

x = [1,2,3,5,6,7,89,0]
print(dir(x)) #it returns all the attributes and methods with dunder method

print(x.__add__) #info about the method
print(x.__getitem__)

# 2 __dict__ Method :-
''' '__dict__' attribute returns a 'dictionary' representation of an objects attributes it is a 
useful tool for introspection '''

#example - 

class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.version = 1



p = person("Ganesh",23)

print(p.__dict__) #represent attributes and objects in dict format key-value pairs


#3 help() :-
'''the help function is used to documentation for inspect, including a description of an attributes 
and methods'''
#it will give you all the information about the class which you dont know anything about it 
p2 = person("nilesh", 55)
print(help(p2)) #all the description full fledge description of the object.

