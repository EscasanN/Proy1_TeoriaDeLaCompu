import ShuntingYard

print("hi")
file = open("input.txt", "r")
for line in file:
    print(line)
    parts = line.split()
    print(ShuntingYard.ShuntingYard(parts[0]))