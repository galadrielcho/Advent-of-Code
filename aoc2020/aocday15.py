def speak(lastSpoken, turn):
    if lastSpoken not in nums:
        nums[int(lastSpoken)] = turn - 1
        retval = 0

    else:
        retval = turn - 1 - nums[lastSpoken]
        nums[lastSpoken] = turn - 1

    return retval


inp = open("aocday15.in", "r")
out = open("aocday15.out", "w")

nums = {}


starting = inp.readline().split(",")

for i in range(len(starting)):
    nums[int(starting[i])] = i + 1

turn = len(starting) + 1
lastSpoken = starting[len(starting) - 1]

while turn <= 30000000:
    lastSpoken = speak(lastSpoken, turn)

    turn += 1

print(lastSpoken)


