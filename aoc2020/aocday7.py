def setContains(line):
    linelist = line.split(" ")
    color = linelist[0] + linelist[1]
    line = line.strip(linelist[0] + " " + linelist[1] + " bags contain ")

    a = ' '.join([i for i in line if i.isdigit()])
    amounts = a.split()
    line = ''.join([i for i in line if not i.isdigit()])

    l = line.strip().split(",")
    for i in (0, len(l) - 1):
        l[i] = l[i].strip().strip(".")
        if len(l[i].split()) > 1:
            l[i] = l[i].split()[0] + l[i].split()[1]

        containing = []
        for i in l:
            if i != "herbags":
                if len(i.split()) > 1:
                    i = i.split()[0] + i.split()[1]
                containing.append(i.strip())
            else:
                amounts = []
    colorContains[color] = [containing, amounts]

def containsGold(color):
    if len(colorContains[color][0]) == 0:
        return False
    elif "shinygold" in colorContains[color][0]:
        return True
    else:
        c = False
        for s in colorContains[color][0]:
            c = containsGold(s) or c
        return c

def countContains(color):
    total = 0
    for i in colorContains[color][1]:
        total += int(i)
    something[0] += total

    a = 0
    for i in colorContains[color][0]:
        if len(colorContains[color][1]) == 0:
            break
        times = int(colorContains[color][1][a])
        for d in range(times):
            print(i + str(d))
            countContains(i)
        a += 1


inp = open("aocday7.in", "r")
out = open("aocday7.out", "w")

# color int values
colorContains = {}
something = [0]

for line in inp:
    setContains(line)


colors = list(colorContains.keys())
countContains("shinygold")

out.write(str(something[0]))
out.close()