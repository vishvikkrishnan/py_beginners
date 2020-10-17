#find number of times a number occurs in an array
def count__(nums, n):
    count = 0
    i = 0
    while i < len(nums):
        if nums[i] == n:
            count = count+1
        i = i+1    
    return count

def count_array(nums):
    count = {}
    j = 0
    for i in nums:
        if i not in count:
            count[i] = count__(nums, i)
    print(count)

le = int(input('How many elements would you liketo enter? '))
nums = []

for i in range(0, le):
    item = int(input('Enter element: '))
    nums.append(item)

count_array(nums)
