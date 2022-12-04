with open("4/input.txt", "r") as file:
  lines = file.read().split("\n")

count = 0

def is_slice_in_list(s,l):
    len_s = len(s)
    return any(s == l[i:len_s+i] for i in range(len(l) - len_s+1))

def get_fields(input):
  splitted_input = input.split("-")
  first, second = int(splitted_input[0]), int(splitted_input[1])

  list_of_ints = list(range(first, second+1))

  return [str(i) for i in list(range(first, second+1))]

for line in lines:
  split_line = line.split(",")
  first_elf, second_elf = split_line[0], split_line[1]

  first_elf_fields = get_fields(first_elf)
  second_elf_fields = get_fields(second_elf)

  # if (is_slice_in_list(first_elf_fields, second_elf_fields) or is_slice_in_list(second_elf_fields, first_elf_fields)):
  #   count += 1

  if (len(first_elf_fields) > len(second_elf_fields)):
    for field in first_elf_fields:
      if field in second_elf_fields:
        count += 1
        break
  elif (len(first_elf_fields) < len(second_elf_fields)):
    for field in second_elf_fields:
      if field in first_elf_fields:
        count += 1
        break
  else:
    for field in first_elf_fields:
      if field in second_elf_fields:
        count += 1
        break

print(count)