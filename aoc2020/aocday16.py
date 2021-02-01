def valid(n):
    for v in n:
        val = int(v)
        valid = False
        for r in ranges:
            fo = r[0].split("-")
            so = r[1].split("-")
            if (int(fo[0]) <= val <= int(fo[1]) or (int(so[0]) <= val <= int(so[1]))):
                valid = True
        if not valid:
            inv.append(val)
            return False
    return True



inp = open("aocday16.in", "r")
out = open("aocday16.out", "w")

ranges = []
mytic = []
nearby = []


status = 0
for line in inp:
    if line.strip() == "":
        pass
    elif line == "your ticket:\n":
        status = 1
    elif line == "nearby tickets:\n":
        status = 2
    else:
        if status == 0:
            l = line.split(":")[1].strip().replace(" ", "").split("or")
            ranges.append(l)
        if status == 1:
            mytic = line.strip().split(",")
        if status == 2:
            nearby.append(line.strip().split(","))


inv = []
for n in nearby:
    valid(n)

for i in inv:
print(sum(inv))