#start with a hard coded list a = [3,4,5,86,34,2,3,4,7,33,44,66,88,34,32,11,22]
# and write a program (bubble sort) to sort the list in ascending order - bubble sort


a = [3,4,5,86,34,2,3,4,7,33,44,66,88,34,32,11,22]

def bubble_sort(list_a):
    n = len(a)-1
    #we dont want to check the last elements
    sorted = False
    while not sorted:
        sorted = True
        for i in range(0, n):
            if list_a[i] > list_a[i+1]:
                #if item in a list at left is greater than item in alist at right
                sorted = False
                list_a[i], list_a[i+1] = list_a[i+1], list_a[i]
                #then we should swap the their position
    return list_a

bb = (bubble_sort(a))
print(f"the sorted list in ascending order is:{bb}")







