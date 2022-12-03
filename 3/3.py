import string

values = {letter: index + 1 for index, letter in enumerate(string.ascii_lowercase + string.ascii_uppercase)}
sum_of_all = 0

with open("3/input.txt", "r") as file:
  lines = file.read().split("\n")

for line in lines:
  item_count = int(len(line) / 2)
  first_half, second_half = set(line[:item_count]), set(line[item_count:])
  common_letter = list(first_half&second_half)[0]

  print(f"Common: {common_letter} –> {values[common_letter]}")
  sum_of_all += values[common_letter]

start = 0
sum_of_all = 0

print(len(lines))

for n in range(0, len(lines)+1, 3):
  if n == 0:
    continue

  current_lines = lines[start:n]

  common = list(set(current_lines[0])&set(current_lines[1])&set(current_lines[2]))[0]

  print(f"Common: {common} –> {values[common]}")

  sum_of_all += values[common]

  start = n

print(sum_of_all)