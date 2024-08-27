#multiple inheritance - 
'''multiple inheritance is the powerful feature in object oriented programming that allows a class to inherit programming 
that allows a class to inherit attributes and methods from multiple parellel classes that can be useful 
in situations where to inherit functionality from both multiple sources'''


#syntax  -
'''class childclass(parentclass1, parentclass2, parent class):
#####class body'''


#Example 1 :

class employee: #first class
    def __init__ (self,name):
        self.name = name

class dancer:
    def __init__(self,dance):
        self.dance = dance
        
    def show(self):
        print(f"The dance is {self.dance}")


class danceremployee(dancer,employee):
    def __init__ (self,name,dance):
        self.name = name
        self.dance = dance


p1 = danceremployee("hritik","hip-hop")

print(p1.name)
print(p1.dance)

p1.show() #parent class method

print(danceremployee.mro()) #this inbuilt method provides the classes by which it inherited(dancer,employee)

# mro -method resolution order

##################################################################################################

#multilevel inheritance :
'''multilevel inheritance is the type of the inheritance in object oriented programming where 
a derived class inherits from another derived class this type of inheritance allows you to build 
a hierarchy of classes where one class build upon another leading more specialized class'''

#syntx - 
'''class baseclass:
        #base class body
        
    class derived class(base class):
        #derived class body
        
    class derived class2(dervied class1):
        #derived class 2 body
        # '''


#example 1


class animals: #parent class
    def __init__(self,name,species):
        self.name = name
        self.species = species

    def show_details(self):
        print(f"name :{self.name}")
        print(f"species:{self.species}")

class dog(animals): #derived class 1
    def __init__(self, name, breed):
        super().__init__(name, species = "dog") #parent class constructor
        self.breed = breed #new parameter breed

    def show_details(self):
        super().show_details()
        print(f"breed:{self.breed}")


class german_shepherd(dog): #derived class 2
    def __init__(self,name,colour):
        super().__init__(name,breed="german shepherd") #here parent class is derived class 1
        self.colour = colour #new parameter colour

    def show_details(self):
        super().show_details()
        print(f"colour:{self.colour}")


g = dog("rocky","golden retriever") #derived class 1 input
g.show_details()



g2  = german_shepherd("dhruv","brown") #derived class 2 input
g2.show_details()


g3 = animals("fish","salmone") #parent class input
g3.show_details()


print(german_shepherd.mro()) #gives the method resolution order



################################################################################################################

#Hybrid inheritance -
'''
Hybird inheritance is a combination of the 'multiple' and the 'single' inheritance. in object oriented programming
it is a type of inheritance in which multiple inheritance is used to inherit the properties of base classes. into
a single derived class and single inheritance is used to inherit the properties pf the derived class into su- derived
class '''

#syntax -
''' class baseclass:
        pass
    class derived1(baseclass):#single inheritance
        pass                                           <hierarchical inheritance (multiple classes inherit same parent class)
    class derrived2(baseclass):#single inheritance
        pass
    class derived3(derived1,derived2): #mutiple inheritance 
        pass'''



#hierarchical inheritance - 
'''hierarchical inheritance is a type of inheritance in oop where multiple sub-classes inherit properties from
a single base class in other words "a single base class acts as a prent class for multiple sub-classes'''

'''this is a way of establishing relationship beteween classes in hierarchical manner '''

#syntax -

'''
class baseclass:
    pass
class childclass1(baseclass): #parent class
    pass                                   = (hierarchical inheritace)
class childclass2(baseclass): #parent class
    pass
class childclass3(baseclass1):
    pass'''
