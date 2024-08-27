#local an global variable
'''
"local variable" - local variable is the variable which can be called in the 
perticualr function in which it is declared.

"Global variable" - global variable is the variable which can be accessible 
by the any function in the code.

'''

# global variable example

x = 10
'''
print(x)

def myfunction ():
    global x #by using global keyword this will change global variable
    x = 55 

    y = 50 #local variable 

    print(y) #it will print local variable value cause it is in the function.
    print(x) #it will print local variable value cause it is in the function.

myfunction()
print(x) #it will print 55 cause we changed the global variale value by using 'global x'.
'''

###################################################################################

#file I/O in python:

#1 open - this function is used to open any type of the file it only opens it does not read or prints.
      # f = open ('file.txt', 'r') "r" defines it going to read it and "w" define write mode
#2 read - this function is used to read the actual file contents and we can print also.
''' f = open ('file.txt', 'r')
       text = f.read()
       print(text)
       f.close '''
# rt - text file       ,   rb- binary file(jpeg,ex)

#3 append - adding content withut removing previous
#          'a' - used for append

##################################################
#example 1 
'''
f = open("Python_Revision_challenge/hello.txt", 'r') #read 
print(f)#not in readable format

text = f.read() #reads and print file content
print(text)
f.close() #closing file'''


#example 2
 
'''f = open("Python_Revision_challenge/hello.txt", 'w')#used to add content
f.write("hello there!") #deletes pervious content and writes new
f.close
'''

#example 3

'''
f = open("Python_Revision_challenge/hello.txt", 'a') #to add content without removing previous
f.write("hello there my name is ganesh ") #adds the content at the end
f.close
'''

#example 4 (write function)

'''with open("Python_Revision_challenge/hello.txt", 'a') as f: # with - handles automatically closing the file as loop ends
    f.write("hey i am inside the hello")
    #without using the f.close
'''


###########################################################################################

#read, readlines, write lines methods - 

#1 readlines - line by line
'''The realine method reads a singel line from file and if 
    want to read multiple line we need to use the loop'''

# example 1 #this loop prints line one by one
'''f = open('Python_Revision_challenge/hello.txt', 'r')
while True:
    line = f.readline()
    if not line:
        break
    print(line)

# example 2  #reads all the line in a single take and returns in the list format '''

'''f = open('Python_Revision_challenge/hello.txt', 'r')
while True:
    line = f.readlines()
    if not line:
        break
    print(line)

'''
#write lines - it is used to write sequence of string to a file , the sequence can be list, tuple.etc

#example 1

f = open('Python_Revision_challenge/hello.txt', 'w') #adds line one by one
line = ['line \n', 'line2 \n', 'line3 \n']
f.writelines(line)
f.close