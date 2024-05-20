#get a list a = [2,3,4,55,33,4,55,343,66,77,88,99] and write a program to browse over this list and print previous number and current number


a = [2,3,4,55,33,4,55,343,66,77,88,99]

for index in range(len(a)-1):
    print(f"first {a[index]}, second {a[index+1]}")


    
    
    