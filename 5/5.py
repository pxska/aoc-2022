matrix = []
my_dict = {}
moves = []

with open("5/input.txt", "r") as file:
  lines = file.read().split("\n")

starting_moves = False
for line in lines:
  row = []

  if line == "":
    starting_moves = True
    continue

  if (starting_moves):
    print(line)
    moves.append(line)
    continue

  line = line.replace("    ", " [0] ")

  splitted = line.split(" ")

  for element in splitted:
    if element == "":
      continue
    else:
      row.append(element.replace("[", "").replace("]", ""))

  matrix.append(row)

iterator = 1
for element in matrix:
  if (element == []):
    break

  line_number = 1

  for letter in element:
    if line_number in my_dict:
      my_dict[line_number] += letter
    else:
      my_dict[line_number] = letter

    line_number += 1

  iterator += 1

for key in my_dict:
  my_dict[key] = my_dict[key][::-1][1:].replace("0", "")

print(my_dict)
print(moves)

for move in moves:
  i = 0
  print(move.split(" "))
  x, amount, y, stack_from, z, stack_to = move.split(" ")

  # while int(i) < int(amount):
  #   my_dict[int(stack_to)] += my_dict[int(stack_from)][-1]
  #   my_dict[int(stack_from)] = my_dict[int(stack_from)][:-1]

  #   i += 1

  my_dict[int(stack_to)] += my_dict[int(stack_from)][-int(amount):]
  my_dict[int(stack_from)] = my_dict[int(stack_from)][:-int(amount)]

end_str = ""

for k, v in my_dict.items():
  end_str += v[-1]

print(end_str)