#get a list a = [2,3,4,55,33,4,55,343,66,77,88,99] and write a program to find list of
# non adjacent numbers of every number.

a = [2,3,4,55,33,4,55,343,66,77,88,99]


def adjecent_numbers(nums):
    adj_nums = []
    for i in range(len(nums)-1):
        if nums[i]+1 == nums[i+1]:
            adj_nums.append((nums[i], nums[i+1]))
    return adj_nums

adj =(adjecent_numbers(a))
print(f"the pairs of the adjecent number is: {adj}")