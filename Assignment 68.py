#get a list a = [2,3,4,55,33,4,55,343,66,77,88,99] and write a program to find maximum
# sum of non-adjacent numbers

a = [2,3,4,55,33,4,55,343,66,77,88,99]


def sumadj(list_a):
    adjecent = []
    sum_adjnum = []
    for i in range(len(list_a) - 1):
        if list_a[i] + 1 == list_a[i + 1]:
            adjecent.append((list_a[i], list_a[i+1]))
            sum_adjnum.append(list_a[i] + list_a[i+1])
            maximum = max(sum_adjnum)

    return adjecent , maximum


lst,sum = sumadj(a)
print(f"the list of the adjecent paris is:{lst}")
print(f"the maximum sum of the adjecent paris is:{sum}")






