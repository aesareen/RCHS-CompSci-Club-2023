thanksgiving_foods = ["Mashed Potatoes", "Turkey", "Pumpkin Pie", "Apple Pie", "Mac n' Cheese",]
food = input("Please enter a Thanksgiving food: ")

if food not in thanksgiving_foods:
  print(f"Ew! What is {food}? Don't bring that here!")
else:
  print(f"Yum! I love {food}! Bring it on in!")