#get marks for a student and print grade (if < 30, fail, <50 third class, <60 second class, <70 first class, >=70 distinction, =100 then gold medal


marks = int(input("enter the marks:"))

if marks < 30:
    print("fail")
elif marks < 50:
    print("third class")
elif marks < 60:
    print("Second class")
elif marks < 70:
    print("Third class")
elif marks == 100 :
    print("Gold Medal")
elif marks >= 70:
    print("Distinction")