char_decrypt = {
  'A': 'rock',
  'B': 'paper',
  'C': 'scissors',
  'X': 'loss',
  'Y': 'draw',
  'Z': 'win',
}

shape_score = {
  'rock': 1,
  'paper': 2,
  'scissors': 3
}

outcome_score = {
  'loss': 0,
  'draw': 3,
  'win': 6
}

def choose_based_on_outcome(opponent, outcome):
  if outcome == 'draw':
    return opponent
  elif outcome == 'win':
    if opponent == 'rock':
      return 'paper'
    elif opponent == 'paper':
      return 'scissors'
    else:
      return 'rock'
  else:
    if opponent == 'rock':
      return 'scissors'
    elif opponent == 'paper':
      return 'rock'
    else:
      return 'paper'


with open("2/input.txt", "r") as file:
  lines = file.read().split("\n")

score = 0

for line in lines:
  [opponent_char, outcome_char] = line.split(" ")

  opponent_plays = char_decrypt[opponent_char]
  outcome = char_decrypt[outcome_char]

  me_plays = choose_based_on_outcome(opponent_plays, outcome)

  score += shape_score[me_plays]

  if me_plays == opponent_plays:
    score += outcome_score['draw']
  elif me_plays == 'rock' and opponent_plays == 'scissors':
    score += outcome_score['win']
  elif me_plays == 'paper' and opponent_plays == 'rock':
    score += outcome_score['win']
  elif me_plays == 'scissors' and opponent_plays == 'paper':
    score += outcome_score['win']
  else:
    score += outcome_score['loss']

print(score)