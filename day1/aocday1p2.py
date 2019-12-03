file = open("input.txt", "r")

total = 0
amount_per_mass = 0

for mass in file:
    amount_per_mass = 0
    mass = int(mass.strip())
    fuel = mass
    while (fuel // 3 - 2) > 0:
        fuel = (fuel // 3) - 2
        amount_per_mass += fuel
    total += amount_per_mass

print(total)

