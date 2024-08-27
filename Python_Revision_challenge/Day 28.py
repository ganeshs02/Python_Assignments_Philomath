# Class methods as Alternative Method - 
'''
Constructor - It refers to the special type of method that is automatically gets executed when
object is created from a class. the purpose of the constructor is to initialize the objects
attrubutes allowing the object to be fully functional and ready to use'''

'''
#There are times when you want to create an object in different ways or with different initial values
than what is provided by default constructor .this is where "class" methods are used .

#A class mthods belongs to the class rather than to a instance of class. the common usecase for class
# methods as alternative constuctor is when you want to crete an object from data that is stored in
# differnt format such as string or dict'''

#Example - 

class Employee:
    def __init__(self,name,salary): #"__init__" is a constructor which denotes "initialize".
        Employee.name = name
        Employee.salary = salary

    @classmethod  #here we used class method as an alternative method
    def fromstr(cls,string):
        return cls(string.split("-")[0],int(string.split("-")[1])) #to split given data into needed format
    
e1 = Employee("Nishad","15000")  #it gets 
print(e1.name)
print(e1.salary)


string = "Ganesh-15000" #it gets split into separate - "Ganesh" , "15000"
e2 = Employee.fromstr(string) # to split the string
print(e2.name) #Ganesh
print(e2.salary) #Salary



string1 = "Kiran-15000"
e3 = Employee.fromstr(string1)
print(e3.name)
print(e3.salary)


#####################################################################
 #Super() keyword - the super keyword is mainly used to refer the parent class it is specially useful
 # when the class inherits from multiple parent classes and you want to call method form the one
 # of the parent class.

''' when calss inherit from a parent class it can override or extend the method defined in
 the parent class however sometimes you might want to use the parent class method in the child 
 this is where the 'super' key word comes handy''' 



 #Example -

class Employee:
    def __init__(self,name,id): #constructor 
        self.name = name
        self.id  = id

class Programmer(Employee):
        def __init__(self,name,id,lang):
            super().__init__(name,id) #super keyword (here name and id comes from parent class)
            self.lang = lang #this variable is chil class variable


Ganesh = Employee("Ganesh Surle", "001")
Nikhil = Programmer("Nikhil kumbhar", "002","pyhton")


print(Ganesh.name)
print(Ganesh.id)

print(Nikhil.name)
print(Nikhil.id)
print(Nikhil.lang)        


########################################################################################

