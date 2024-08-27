# findout largest range - input: l1:[1,2,3,4,5,6,8,20,21,22,23,24,25,26,33,32,71,87,7]
# ------ hint sort list in ASCENDING ORDER only consider those parts that are consecutive


def find_largest_range(l1):
    l1.sort()
    longest_range = []
    current_range = []
    for i in l1:
        if not current_range:
            current_range.append(l1[i])
        else:
            if l1[i] == l1[i - 1] + 1:  # to check if consecutive
                current_range.append(l1[i])
            else:
                if len(current_range) > len(longest_range):  # to check if not consecutive
                    longest_range = current_range

                else:
                    current_range = l1[i]

    if len(current_range) > len(longest_range):
        longest_range = current_range
        return longest_range


#example 1
l1 = [1, 2, 3, 4, 5, 6, 8, 20, 21, 22, 23, 24, 25, 26, 33, 32, 71, 87, 7]
result = find_largest_range(l1)
print(f"The largest range in the list is {result}")