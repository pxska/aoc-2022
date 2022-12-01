amounts = {}
curr = 0
pos = 1

with open("1/calories.txt", "r") as file:
  lines = file.read().split("\n")

for line in lines:
  if line != "":
    curr += int(line)
  else:
    amounts[pos] = curr
    curr = 0
    pos += 1

ascending = sorted(amounts.values())

first = ascending[-1]
total = sum(ascending[-3:])

print(first, total)