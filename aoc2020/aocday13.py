def part1(cur):
    idd = -1
    while (idd == -1):
        cur += 1
        for a in range(len(buses)):
            if cur % buses[a] == 0:
                idd = buses[a]
                out.write(str(idd * (cur - start)))
                break
    return str(idd * (cur - start))


def part2():
    pass


inp = open("aocday13.in", "r")
out = open("aocday13.out", "w")

start = int(inp.readline())
cur = start - 1
# .replace("x,", "").replace(",x", "").
ids = inp.readline().split(",")
buses = []

part2()

# for i in range(len(l2)):
#     buses.append(int(l2[i]))


