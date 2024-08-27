# write a function to study pass by value and pass by reference
# (write a function that accepts one variable and one list, increment variable inside the
# function by 1 and print the variable inside function and print variable before and after
# function call. inside function add 3 to all the elements of the list. print list inside function
# and before and after function call)

var1 = int(input("enter any integer"))
list1 = list(map(int, input("enter list of numbers").split()))

print(f"before function call var1: {var1}")
print(f"after function call list1: {list1}")


# print(var1,list1)

def after(var1, list1):
    var1 += 1  # incrementing the variable by 1
    for i in range(len(list1)):
        list1[i] += 3


after(var1, list1)

print(f"after function call var1:{var1}")
print(f"after function call list1: {list1}")
