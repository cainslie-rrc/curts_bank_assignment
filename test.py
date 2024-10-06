poop = input("hello? ")
poop = float(poop)


one = "*****"
two = "*****"
three = f"cool number {poop}"

list = [one, poop, two]

for line in list:
    print(line)

poop = poop + 10

for line in list:
    print(line)

print(poop)

print(list)
