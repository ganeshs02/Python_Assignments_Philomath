# smallest difference between two numbers from two lists (one number from each list).
# Input l1: [2,4,6,8], l2:[3,10,18,19] .. Output is 1 for this example

list1 = [2,4,6,8]
list2 = [3,10,18,19]

def lst_compare(list1, list2):
    min_diff = float('inf')
    element1, element2 = 0, 0
    for i in list1:
        for j in list2:
            diff = abs(i - j)
            if diff < min_diff:
                min_diff = diff
                element1, element2 = i, j
            else:
                print(f"the minimum difference is: {min_diff} and elements are {element1} and {element2}")
                return " "


print(lst_compare(list1, list2))
