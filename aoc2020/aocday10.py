inp = open("aocday10.in", "r")
out = open("aocday10.out", "w")
arrangements = {}

def findJoltDiff():
    onejolt = 0
    threejolt = 0
    for n in range(len(volts) - 1):
        if volts[n + 1] - volts[n] == 1:
            onejolt += 1
        if volts[n + 1] - volts[n] == 3:
            threejolt += 1
    print(onejolt)
    print(threejolt)
    return onejolt * threejolt

# connect to 1-3 jolts lower
# last always has to be highest + 3
def validArrangement(num):
    if num in arrangements:
        return arrangements[num]
    if num == volts[len(volts) - 1]:
        return 1
    else:
        arrs = 0
        for i in range(num + 1, num + 4):
            if volts.count(i) >= 1:
                arrs += validArrangement(i)
        arrangements[num] = arrs
        return arrs


volts = [0]

for line in inp:
    volts.append(int(line))

volts.sort()
volts.append(volts[len(volts) - 1] + 3)


out.write(str(validArrangement(0)))