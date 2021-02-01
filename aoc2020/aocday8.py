def checkInfiniteLoop():
    visited = [False] * len(lines)
    pos = 0
    acc = 0
    while (visited[pos] == False):

        visited[pos] = True
        if lines[pos][0].strip() == "acc":
            acc += int(lines[pos][1])
            pos += 1
        elif lines[pos][0].strip() == "jmp":
            pos += int(lines[pos][1])
        elif lines[pos][0].strip() == "nop":
            pos += 1
        if pos == len(lines):
            return [True, acc]

    return [False, acc]


inp = open("aocday8.in", "r")
out = open("aocday8.out", "w")

lines = []
final = 0
for line in inp:
    l = line.split()
    lines.append(l)

for l in lines:
    if l[0] == "nop":
        l[0] = "jmp"
        a = checkInfiniteLoop()
        if (a[0]):
            final = a[1]
            break
        else:
            l[0] = "nop"
    if l[0] == "jmp":
        l[0] = "nop"
        a = checkInfiniteLoop()
        if (a[0]):
            final = a[1]
            break
        else:
            l[0] = "jmp"

out.write(str(final))
out.close()