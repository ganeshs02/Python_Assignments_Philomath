'''exception handlig in python''' #- it means the process of responding to the
#unexpected events occured when programs runs.
#which deals with these events to avoid program crashing.
#without this process exception will distrupt the normal functioning of program.

#1 example - 

'''a = input("enter an integer:")
print(f"multiplication table of an {a}")

try: #try is used to run below program to chekc for errors
    for i in range(1,11):
        print(f"{int(a)}*{i} = {int(a)*i}")

except ValueError: #except is used to handle the erros (to catch value error)
    print("you have entered invalid input")

except Exception as e: #to catch all other errors
    print(f"an error occured : {e}")'''


#2 example - multiline and multiple execption handling

try:
    num = int(input("enter an integer:"))
    a = (6,3)
    print(a[num]) #try to access tuple element at given index

except ValueError: #to handle invalid input
    print("entered the invalid input")

except IndexError: #handle index out of range
    print("index error")