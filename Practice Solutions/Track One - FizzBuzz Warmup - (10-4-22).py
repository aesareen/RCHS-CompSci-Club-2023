import math

num = int(input("Hello there! Please enter an integer value: "))

if num % 5 == 0 and num % 11 == 0:
  print("Filnav")
elif num % 5 == 0:
  print("Fillip")
elif num % 11 == 0:
  print("Arnav")
else:
  print(f"{num} is just a normal number. How lame!")