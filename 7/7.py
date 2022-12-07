file_structure = {}
directory_sizes = {}
total_available = 70000000
needed_to_run_update = 30000000

with open("7/input.txt", "r") as file:
  lines = file.read().split("\n")

def get_dir_sizes_recursively(directory):
  size = 0

  for file in file_structure[directory]:
    type, name = file.split(" ")

    if not type.isdigit() and f'{directory}{name}/' in file_structure:
      if type.isdigit():
        size += int(type)
      size += get_dir_sizes_recursively(f'{directory}{name}/')

    if type.isdigit():
      size += int(type)

  return size

current_dir = ""

for line in lines:
  if "$ cd " in line:
    _, _, directory = line.split(" ")

    if directory == "..":
      current_dir = current_dir[:current_dir.rfind("/", 0, len(current_dir) - 2) + 1]
    elif directory != "/":
      current_dir += directory + "/"
    else:
      current_dir = directory
  if "$ ls" in line:
    file_structure[current_dir] = []
  if "$" not in line:
    file_structure[current_dir].append(line)

for directory in file_structure:
  size = 0;

  directory_sizes[directory] = get_dir_sizes_recursively(directory)

sum_of_all = 0
closest = 0
stop = False

for directory in directory_sizes:
  if len(directory.split("/")) == 3:
    sum_of_all += int(directory_sizes[directory])

number_needed = needed_to_run_update - (total_available - sum_of_all)
sorted_dir_sizes = sorted(directory_sizes.items(), key=lambda x: x[1], reverse=False)

stop_code = False
for (k, v) in sorted_dir_sizes:
  if (stop_code):
    closest = v
    break
  elif (int(v) > number_needed):
    stop_code = True

print(closest)
