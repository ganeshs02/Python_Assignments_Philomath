list1 = [45, 65, 25, 78, 96, 85, 96, 86, 25, 63]
list2 = []

for element in list1:
    list2.append(element)
    list2.append(element + element / 18)

print(list2)
