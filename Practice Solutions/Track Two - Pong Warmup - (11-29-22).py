#Track Two:
colors = ["Red", "Blue", "Green", "Yellow", "Purple"]
def check(color):
  if color not in colors:
    print("I am sorry that is an invalid color!")
    return False
  return True

player_count = int(input("Welcome to CompSci Pong! How many players are playing today? "))
player_names = []
player_colors = []

for i in range(player_count):
  if player_count > len(colors):
    print("Too many players!")
    break
  player = input(f"Hello Player {i+1}! What is your name? ")
  color = input(f"Welcome {player}! What color would you like to be? ")
  if not check(color):
    pass
  if color in player_colors:
    print("That color has already been chosen!")
    break
  else:
    player_names.append(player)
    player_colors.append(color)

if player_count == len(player_names):
  print("Great, this is what I have!")
  [print(f"Player {i+1}: {player_names[i]}, Color: {player_colors[i]}") for i in range(player_count)]
