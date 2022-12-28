class Player:
  @classmethod
  def from_csv(cls, csv_str):
    name, age, nationality = csv_str.split(",")
    return cls(name, int(age), nationality)
  
  def __init__(self,name,age,nationality):
    self.name = name
    self.age = age
    self.nationality = nationality

  def print(self):
    print(f"{self.name} is {self.age}-year old player from {self.nationality}")

def create_player(player):
  print(len(player))
  if len(player) != 3:
    return Player.from_csv(player)
  else:
    name,age,nationality = player
    return Player(name,age,nationality)

messi = ["Lionel Messi", 35, "Argentina"]
ronaldo = "Cristiano Ronaldo,37,Portugal"
neymar = "Neymar,30,Brazil"

messi = create_player(messi)
ronaldo = create_player(ronaldo)
neymar = create_player(neymar)

messi.print()
ronaldo.print()
neymar.print()