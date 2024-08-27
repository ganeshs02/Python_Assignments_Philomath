#ask user to enter 10 numbers store them in list and print list,
# count the number of times 10 is present in the list and print the result


input1 = input("enter 10 numbers using spaces:").split()

if len(input1) != 10:
    print("enter exactly 10 numbers")
else:
    print("list of the numbers",input1)

count = input1.count('10')
print(count)


