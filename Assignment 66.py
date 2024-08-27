#start with a hard coded list a = [3,4,5,86,34,2,3,4,7,33,44,66,88,34,32,11,22]
# and write a program (bubble sort) to sort the list in descending order - bubble sort

a = [3,4,5,86,34,2,3,4,7,33,44,66,88,34,32,11,22]


def bubble_sort_rev(list_a):
    n = len(a)-1
    sorted = False
    while not sorted:
        sorted = True
        for i in range(0, n):
            if list_a[i]<list_a[i+1]:
                list_a[i], list_a[i+1] = list_a[i+1], list_a[i]
                sorted =False

    return list_a


bb = (bubble_sort_rev(a))
print(f"the sorted list in the descending order is: {bb}")





