inp = open("aocday12.in", "r")
out = open("aocday12.out", "w")

coords_w = [10, 1, 1]
coords_s = [0,0]
directs = ["N", "E", "S", "W"]

def move(instr, dist):
    if instr == "N":
        coords_w[1] += dist
    elif instr == "S":
        coords_w[1] -= dist
    elif instr == "E":
        coords_w[0] += dist
    elif instr == "W":
        coords_w[0] -= dist
    elif instr == "L":
        times = int(dist / 90)
        for i in range(0, times):
            temp = [coords_w[0], coords_w[1]]
            coords_w[0] = int(-1 * (coords_w[1] - coords_s[1]) + coords_s[0])
            coords_w[1] = int(temp[0] - coords_s[0] + coords_s[1])

    elif instr == "R":
        times = int(dist / 90)
        for i in range(0, times):
            temp = [coords_w[0], coords_w[1]]
            coords_w[0] = int(coords_w[1] - coords_s[1] + coords_s[0])
            coords_w[1] = int(-1 * (temp[0] - coords_s[0]) + coords_s[1])

    elif instr == "F":
        deltax = coords_w[0] - coords_s[0]

        deltay = coords_w[1] - coords_s[1]

        for i in range(0, dist):
            coords_s[0] += deltax
            coords_w[0] += deltax
            coords_s[1] += deltay
            coords_w[1] += deltay


for line in inp:
    line = line.strip()

    move(line[0], int(line[1:]))
    print("Ship " + str(coords_s))
    print("Way " + str(coords_w))
    print()

print(abs(coords_s[0]) + abs(coords_s[1]))
out.write(str(abs(coords_s[0]) + abs(coords_s[1])))