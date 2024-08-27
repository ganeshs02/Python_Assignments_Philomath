#decorators in python - decorators are a powerful and variable tool that allows you to modify the behaviour
#of the function or the method without modifying its source code.

# it is a function that takes anoter function as a argument and return a new function that modifies 
#the behaviour of the original function 

#example - 
'''
def greet(fx): #assigned greet
   def mfx(*args ,**kwargs):# *args - tuple  and **kwargs - dictionary 
        print("Good morning!")
        fx(*args,**kwargs)
        print("Thank you for using this function ")
   return mfx
    
@greet #assigned greet function
def hello():
    print("hello world")

@greet
def add(a,b):
    print(a+b)


hello() #instead of greet(hello)() - mfx function gets called and prints goood morning - then hello() - thank you for..
add(1, 2)#instead of greet(add)(1, 2)
'''

##########################################################################################################
#Getters and Setters in Python  -  
#Getters - A getter method is used to access the value of a private attribute.
#  It is usually defined with the @property decorator in Python.

#setters - A setter method is used to set or update the value of a private attribute.
#  It is defined with the @<property_name>.setter decorator in Python.
'''
class myclass:
    def __init__(self,value):
        self._value = value

    def show(self):
        print(f"value is {self._value}")
 
    @property  #is getter 
    def ten_value(self):
        return 10 * self._value


    @ten_value.setter
    def ten_value(self, new_value):
        self._value = new_value/10


obj = myclass(10)
obj.ten_value = 67
print(obj.ten_value)
obj.show()
'''

#################################################################################################################
#INHERITANCE - when a class derives from another parent class . the derived child class will inherit properties
#and methods form the parent class adn in addtion it can has its own properties and methods. 
'''
Types 
1. single inheritance
2.multiple inheritance 
3.multilevel inheritnce
4.hierarchical inheritance
'''
'''
"child class can have the all the method of parent class and its own new methods but parent class does not have 
the methods from the child class this is called inheritance'''

# example 

#parent class
class employee: 
    def __init__(self, name, id):
        self.name = name
        self.id = id
    
    def showdetails (self):
        print(f"the name of the employee is: {self.name} and id is {id}")

#child  class
class programmer(employee): #employee is the name of parent class
    def showlanguage(self):
        print("the default language is python")



e1 = employee("sharad bailkar",18) #object created
e1.showdetails()

e2 = programmer("ganesh surle",22)#child class
e2.showdetails() #parent class method
e1.showlanguage()# it will give error cause parent class does not have child class methods


