# Dictionary (mutable)

information = {"kiran":"database", "ganesh": "web server", "nishad": "database ad server", "nikhil": "hybernet"}

print(information)

#1 to access elements 
print(information.get("nikhil"))
print(information["ganesh"])

#2 to print multiple values 
print(information.keys())
print(information.values())

#3 "in" keyword in dictionary {}= key []= value
for key in information.keys():
    print(f"information {key} is {information[key]}")


#4 to items in keyvalue format
print(information.items())
for key, value in information.items():
    print(f"the value corresponding to the key {key} is {value}")


#5 update (to add one to dict to another)

ep = {122:55, 555:698, 888:999, 874:965}

ep2 = {582:896, 365:145}

ep.update(ep2)
print(ep)

#6 clear (clears all the elements in selected dict)

ep2.clear()
print(ep2)

#7 pop (to pop out the selected index values)

ep.pop(122)
print(ep)

#8 pop item (to pop out last items in the dictionary)
ep.popitem()
print(ep)

#9 del  (to delete the index element)
del ep[555]
print(ep)

#################################################################


#for loop with else - else get executed when loop value get over
# we can use else statement with while and for

#example 1

'''for i in range(5):
    print(i)
    if i == 4:
        print(i)
else: #else get executed when loop value is over
    print("no'i'")

'''
#example 2
for i in []:
    print(i)
    if i == 4:
        print(i)
else:
    print("no'i'")
