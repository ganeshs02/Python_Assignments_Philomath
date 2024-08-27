
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
        self.books = {}

    def addbook(self, book , author): #for adding books
        self.books[book] = author
        self.nobooks = len(self.books)
        #print(f"you added:{book} to the library thank you!")
        print(f"current book count is {self.nobooks}")
    
    def showinfo(self): #to show the no of books and thier info
        print(f"the library has {self.nobooks} books right now and the books are:\n")
        for book, author in self.books.items():
            print(f"{book} by - {author}")

    def borrow(self, book): #to borrow the book from the library
        if book in self.books:
            author = self.books.pop(book) #deleting key-value pair from the avilable book count(dict)
            self.nobooks = len(self.books)
            print(f"your borrowed:{book} by {author}")
            print(f"current book count is {self.nobooks}")
        else:
            print(f"Sorry the {book} is currently not available!")
            print(f"current book count is : {self.nobooks}")
        
        
#############################################################################################
l1 = Library()
l1.addbook("Atomic Habits","james clear") #adding book in the library
l1.addbook("Rework", "json fried")
l1.addbook("Mindset", "carol dweck")
l1.addbook("Deepwork", "cal newport")
l1.addbook("Masala King", "Dhananjay datar")



#print(l1.__dir__()) #shows the available methods in the objct of library class
####################################################
#l1.showinfo()#getting books info in library

################################################################

#l1.borrow("Rework") #borrowing the book from the library




###################################################################################################
print("welcome to the library🙂😊")

while True:
    space = ("                                                                                               ")    
    choice = input("which service do you wnat🤔? enter 1 for books info , enter 2 for borrowing book, enter 3 for adding book: , enter 4 for exit \n")

    if choice == "1":
        l1.showinfo()
    elif choice == "2":
        bminus = input("enter which book name you want to borrow? : \n")
        l1.borrow(bminus)

    elif choice == "3":
        badd = input("enter the book which you want to add in library: \n")
        bauth = input("enter the name of author: \n")
        l1.addbook(badd,bauth)
    elif choice == "4":
        break
    