#classes and objects
#class - ince class created we can create multiple objects by using default values of class by just modifying it.
#objects - it is an instance of the class used to access properties of the class.

#self parameters - the self parameter is and reference to current class and used to access variables 
#that brings to the class.
########################

#creating a class

class person : 
    name = "nitin"
    occupation = "software developer"
    networth = 10000000
    
    #constructor method
    def __init__(self,name,occupation):
        print("hey i am a person")
        self.name = name
        self.occupation = occupation
        #CREATING METHOD
    def info(self): #all the methods should be inside class
        print(f"{self.name} is a {self.occupation}")
''' 
self - is the parameter is an reference to the current instance of the class
and is used to acces variables that belong to the class
#" wo object jiske liya ye method call kiya ja raha hain"
'''


#CREATING OBJECT
#added values for the constructor
a = person("Ganesh", "CEO") #creating new oobject
b = person("nilesh", "cmo")
#
b.name = "soma"
b.occupation = "HR"
a.name = "vishal" #it renames name value for a object
a.occupation = "data analyst"
#print(a.name , a.occupation)
a.info()
b.info()
#c.info() #it will print default values 


###############################################################
# Constructors - constructor is the simple method of creating the objects in the class. it is a unique functions 
#that gets called automatically when an object is created.

#creting class
class animal:
    def __init__(self,name,habitat):
        #constructor invoke automatically when obj is created
        print("hello i am a animal")
        self.name = name
        self.habitat = habitat

    #creating method for calling the created
    def info(self):
        print(f"{self.name}, {self.habitat}")

a = animal("rabbit","herbivorous")#animal is taken as a first arg
b = animal("tiger", "carivorous") #

a.info()
b.info()