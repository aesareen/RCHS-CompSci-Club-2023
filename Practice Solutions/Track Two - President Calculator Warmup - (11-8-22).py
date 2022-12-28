#Track Two
class Candidate:
  def __init__(self, name, gender, party, age, experience, wealth):
    self.name = name
    self.gender = gender
    self.party = party
    self.age = age
    self.experience = experience
    self.wealth = wealth
  def calculate_chances(self):
    chance = 0
    if self.gender == "male":
      chance += 4
    if self.party == "Democrat":
      chance += 45
    elif self.party == "Republican":
      chance += 41
    else:
      chance -= 8
    if self.age <= 40:
      chance += 8
    elif self.age <= 50:
      chance += 5
    elif self.age >= 70:
      chance -= 3
    for _ in self.experience:
      chance += 3
    if self.wealth >= 1000000000:
      chance += 7
    elif self.wealth >= 10000000:
      self.wealth += 2
    
    return f"{self.name.split(' ', 1)[0]} has a {chance}% of becoming president"

trump = Candidate("Donald Trump", "male", "Republican", 77, ["US President"], 3200000000)
biden = Candidate("Joe Biden", "male", "Democrat", 81, ["US President", "Delaware Senator", "Vice President"], 8000000)
bray = Candidate("Shannon W. Bray", "male", "Libertarian", 50, [], 500000)

print(trump.calculate_chances())
print(biden.calculate_chances())
print(bray.calculate_chances())