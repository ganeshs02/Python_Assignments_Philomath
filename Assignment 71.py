#get a large list of numbers a = [32,43,55,11,2,3,4,5,66,33,66,7,567,89,87,54,32,12,34,567,333,256,242,121]
# , sort the list and search a user given number in list using binary search technique.

def binary_search(a,target):
    low = 0
    high = len(a) - 1

    while low <= high:
        mid = ((low + high) // 2)
        if a[mid] == target:
            return mid
        elif a[mid] < target:
            low = mid + 1

        else:
            high = mid -1
    return -1
##############################
#example 1

a = [32,43,55,11,2,3,4,5,66,33,66,7,567,89,87,54,32,12,34,567,333,256,242,121]


target = int(input("enter the number: "))

a.sort()
print(f"The sorted list is :{a}")

result = binary_search(a,target)

if result != -1:
    print(f"the target value '{target}' found at the index '{result + 1}' ")
else:
    print(f"The target value you entered '{target}' is not in the list")


