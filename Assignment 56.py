#start with hard coded list say a = [12,3,34,45,88,23,45,63,3,4,69,99] and find  maximum in this list (without using python readymade function)



a = [12,3,34,45,88,23,45,63,3,4,69,99]

def max_value (numbers):
    if not numbers:
        return None
    max_value  = numbers[0]
    for number in numbers[1:]:
        if number > max_value:
            max_value = number
        return max_value

maximum = max(a)
print(maximum)