file = open("input.txt", "r")

total = 0

for i in file:
  i = int(i.strip())
  total += (i//3) - 2

print(total)

