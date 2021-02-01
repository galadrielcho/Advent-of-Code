inp = open("aocday11.in", "r")
out = open("aocday11.out", "w")

grid = []
changedGrid = []

def seatingRound(row):
    changes = 0
    for i in range(len(grid[row])):
        aA = anyAdjacent(row, i, -1, 0) + anyAdjacent(row, i, 1, 0) + anyAdjacent(row, i, 0, -1)
        aA += anyAdjacent(row, i, 0, 1) + anyAdjacent(row, i, -1, -1) + anyAdjacent(row, i, -1, 1)
        aA += anyAdjacent(row, i, 1, -1) + anyAdjacent(row, i, 1, 1)
        if grid[row][i] == "L" and aA == 0:
            changedGrid[row][i] = "#"
            changes += 1
        elif grid[row][i] == "#" and aA>= 5:
            changedGrid[row][i] = "L"
            changes += 1
    return changes


def anyAdjacent(row, pos, deltar, deltapos):
    anyAdjacent = 0
    cont = True
    while cont and 0 <= row + deltar <= (len(grid) - 1) and 0 <= pos + deltapos <= (len(grid[row]) - 1):
        row += deltar
        pos += deltapos

        if grid[row][pos] == "#":
            anyAdjacent += 1
            cont = False
        if grid[row][pos] == "L":
            cont = False
    return anyAdjacent


for line in inp:
    row = []
    for char in line:
        if char != "\n":
            row.append(char)
    grid.append(row)

c = -1
while c != 0:
    c = 0
    changedGrid = []
    for a in range(len(grid)):
        row = []
        for b in range(len(grid[a])):
            row.append(grid[a][b])
        changedGrid.append(row)

    for i in range(len(grid)):
        c += seatingRound(i)

    grid = changedGrid

counts = 0
for a in range(len(grid)):
    for b in range(len(grid[a])):
        if grid[a][b] == "#":
            counts += 1

print(counts)
out.write(str(counts))
