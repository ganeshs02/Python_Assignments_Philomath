#use same hard coded list as given in assignment 3, find total of all numbers in the list

firstlist = [12,3,34,45,88,23,45,63,3,4,69,99]


firstlistsum = sum(firstlist)
print(firstlistsum)

###########  without using the inbuilt function
sum1 =0
for i in firstlist:
      sum1 += i

print(f"final sum is : {sum1}")

