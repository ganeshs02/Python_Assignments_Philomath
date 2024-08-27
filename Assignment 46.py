#write a function to find factors of a number and add them in list

number = int(input("enter any number of your choice:"))


def factors(number):
    list1 = []
    for i in range(1,number+1):
        if number % i == 0:
            list1.append(i)
    return list1



print(factors(number))


