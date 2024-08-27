 #Access Modifiers - access modifiers are used to limit of the class methods and variables outside 
#the calss.

#1 Public access modifiers - all the vaiables in the python are by default public.

#2 private access mdoifers - private accesss modifiers are those members which are accesssible inside 
#the calss not outside the class.

#3. protected access modifiers =  protected is used to describe a member a mthod attriute of a class
#that is intended to be access only by the calss itself and its intended subclasses.
'''
NAME MANGLING - name mangling in python is technique used for the protection of class and subclass
private attributes from being accidently overwritten by subclass names of class private and subcalss.
private attributes are transfrormed by the addtion of the single indexing 
(_(classname)__name)
'''
#exmaple 1

#public

class Employee:
    def __init__(self):
        self.__name = "ganesh"#private attribute
        self._name = "ganesh"#protected attribute

    def _funName(self):#protected attribute
        return "ganesh surle"
    
a =  Employee() #newobject
#print(a.name)# can be publically accessible
###############################################################
#private


b = Employee()
#print(b.__name) #cannot be accessible directly

print(a._Employee__name) #can be accessed indirectly
print(b._Employee__name) #can be accessed indirectly

print(a.__dir__()) #prints(allthe methods in the object)

#######################################################################

#protected 

class Subject(Employee):
    pass

obj = Employee()
obj1 = Subject()

#calling obj employee class
print(obj._name) #output: ganesh_protected
print(obj._funName()) #output: ganesh_surle
#print(obj.__name)


#calling object of Subject class
#print(obj.__name) #output: ganesh_protected
print(obj1._funName())



#################################################################

'''
library management system project - wirte a library class
with no_of_books and books as tow instance variables write
a paragraphs to create a library from this library class
adn show how you can print all boooks and get the nmber of 
books using different methods show that your program
dosent presist the books after the program is stopped.
'''

class Library:
    def __init__(self):
        self.nobooks = 0
        self.books = []

    def addbook(self, book):
        self.books.append(book)
        self.nobooks = len(self.books)
    
    def showinfo(self):
        print(f"the library has {self.nobooks} books and the books are:")
        for book in self.books:
            print(book)

l1 = Library()
l1.addbook("Atomic Habits")

l1.addbook("Rework")

l1.addbook("Mindset")
l1.showinfo()







    