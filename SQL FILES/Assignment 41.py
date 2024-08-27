#write a function to compare two lists, function should return 1 if lists are same and 0
# if lists are not same.

list1 = input("enter list 1").split()
list2 = input("enter list 2").split()

#print(list1)
#print(list2)

def compare (list1,list2):
    if list1 == list2:
        return 1
    else:
        return 0

print(compare(list1,list2))
