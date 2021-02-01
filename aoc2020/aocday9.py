def isValid(num):
    val = False
    for i in range(len(nums)):
        for a in range(len(nums)):
            if nums[i] + nums[a] == num:
                val = True
    return val

def findContSet():
    for i in range(len(nums)):
        s.clear()
        for a in range(i, len(nums)):
            s.append(nums[a])
            if sum(s) == 217430975:
                return True
    return False



inp = open("aocday9.in", "r")
out = open("aocday9.out", "w")

nums = []
s = []

final = 0
for line in inp:
    nums.append(int(line))
    if findContSet():
        s.sort()
        out.write(str(s[0] + s[len(s) - 1]))
        print(s)
        break