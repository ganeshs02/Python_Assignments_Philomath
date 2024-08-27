# write a function to get maximum element of list and second highest element in a list

list1 = (input("enter any string "))


def onetwo(list1):
    list12 = (list1.split())

    list12 = [int(i) for i in list12]

    if len(list12) < 2:
        print("you entered the string with less than 2 elements")

    maxi = sorted(list12)

    max1 = (max(maxi))
    print(f"the largest element in the string list is : {max1}")

    max2 = (maxi[(len(maxi) - 2)])
    print(f"the second largest element is : {max2}")


onetwo(list1)
