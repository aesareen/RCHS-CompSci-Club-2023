#Track One:
colors = ["Red", "Blue", "Green", "Yellow", "Purple"]


player_one_name = input("Hello Player One! What is your name? ")
player_one_color = input(f"Welcome {player_one_name}! What color would you like to be? ")

if player_one_color not in colors:
  print("I am sorry that is an invalid color!")
else:
  player_two_name = input("Hello Player Two! What is your name? ")
  player_two_color = input(f"Welcome {player_two_name}! What color would you like to be? ")
  if player_two_color not in colors:
    print("I am sorry that is an invalid color!")
  else:
    print(f"Great! This is what I have: Player One: {player_one_name}, Color: {player_one_color} \n Player Two: {player_two_name}, Color: {player_two_color}")