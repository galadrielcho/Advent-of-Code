def setMask(l):
    mask = l.split()[2]
    ow_0.clear()
    ow_1.clear()
    xs.clear()
    for i in range(len(mask)):
        if mask[i] == "0":
            ow_0.append(i)
        if mask[i] == "1":
            ow_1.append(i)
        if mask[i] == "X":
            xs.append(i)


def overwrite_1(line):
    l = line.split()
    add = int(l[0][4:-1])
    val = list(bin(int(l[2]))[2:])
    while len(val) < 36:
        val.insert(0, "0")
    for a in ow_0:
        val[a] = '0'
    for b in ow_1:
        val[b] = '1'
    val = "".join(val)

    addrs[add] = val

def overwrite_2(line):
    l = line.split()
    addr = list(bin(int(l[0][4:-1])))[2:]
    val = int(l[2])

    while len(addr) < 36:
        addr.insert(0, "0")
    for b in ow_1:
        addr[b] = '1'
    if len(xs) > 0:
        floating(addr, 0, val)

def floating(addr, pos, val):

    for i in range(2):
        addr[xs[pos]] = "" + str(i)
        s = ""
        for n in addr:
            s += n

        addrs[int(s, 2)] = val

        if pos + 1 < len(xs):
            floating(addr, pos + 1, val)




inp = open("aocday14.in", "r")
out = open("aocday14.out", "w")

ow_0 = []
ow_1 = []
xs = []
addrs = {}



for line in inp:
    if line[:3] == "mas":
        setMask(line)
    else:
        overwrite_2(line)

ks = list(addrs.keys())
ks.sort()
sum = 0

for k in ks:
    # print(str(k) + " " + str(addrs[k]))
    sum += addrs[k]

print(sum)