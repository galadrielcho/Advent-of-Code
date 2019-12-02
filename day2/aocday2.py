file = open("day2input.txt", "r")

nums = file.readline().strip().split(",")

for i in range(len(nums)):
    nums[i] = int(nums[i])
x = 0
while x < len(nums):
    if nums[x] == 99:
        x = len(nums) + 1
    elif nums[x] == 1:
        nums[nums[x+3]] = nums[nums[x+1]] + nums[nums[x+2]]
    elif nums[x] == 2:
        nums[nums[x+3]] = nums[nums[x+1]] * nums[nums[x+2]]
    x += 4

print(nums)



