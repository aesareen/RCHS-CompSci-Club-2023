#Problem Set One:
word = input("Please enter a word in Spanish (Por favor, dame una palabra en español): ")

if word[-1] == "o" or word.split(" ")[0] == "El":
  print(f"{word} is masculine!")
elif word[-1] == "a" or word.split(" ")[0] == "La":
  print(f"{word} is feminine!")
else:
  print(f"I am not sure what gender {word} is")

emotion = input("How are you feeling right now? ")

if emotion == "happy":
  print("Got it! You are feeling 😃")
elif emotion == "awesome":
  print("Woop! Me too, I am also feeling 😁")
elif emotion == "sad":
  print("Aw man, that sucks that you are feeling 😢")
elif emotion == "tired":
  print("Honestly, same 😴")
elif emotion == "Russian":
  print("Добро пожаловать, товарищ 🇷🇺")

#Problem Set Two:
members = ["Arnav", "Fillip", "Luke", "Tushar", "Gabe", "Tathagat", "Aaditya", "Kevin", "Catherine"]

name = input("What is your name? ")

if name in members:
    print(f"Welcome {name}! Enjoy homecoming!")
else:
    age = int(input("How old are you? "))
    if 15 <= age <= 18:
        school = input("What High School do you attend? ")
        if school == "Raleigh Charter":
            print(f"Alright, welcome {name}, but make sure you buy a ticket!")
        else:
            print(f"I am sorry! You don't go to this school. Leave now!")
    else:
        print("What are you doing here? You are aren't even supposed to be at a High School homecoming!")

#Problem Set Three:
number = int(input("Please enter an integer value greater than 0: "))
index = int(input("What is the value of index? "))

b_tree = [8,3,1,6,4,7,10,14,13]

if number == b_tree[index]:
  print('Your number is the selected node')
elif number > b_tree[index]:
  print(f"Your number would be placed to the right of the desired node of {b_tree[index]}")
elif number < b_tree[index]:
  print(f"Your number would be placed to the right of the desired node of {b_tree[index]}")
else:
  print("I don't quite know where your number will be placed!")