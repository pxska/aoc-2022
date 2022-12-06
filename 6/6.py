with open("6/input.txt", "r") as file:
  lines = file.read().split("\n")

for line in lines:
  counts = {}

  for i in range(len(line)):
    end = i + 14

    if end > len(line):
      break

    letters = list(line[i:end])

    for l in letters:
      if l in counts:
        counts[l] += 1
      else:
        counts[l] = 1

    if (len(counts.keys()) == 14):
      print(end, line[i:end], counts)
      break

    counts = {}