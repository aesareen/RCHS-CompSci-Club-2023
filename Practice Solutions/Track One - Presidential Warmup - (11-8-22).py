# Track One
born = input("Were you born in the United States (y/n)? ")
if born == "y":
    time_in_US = int(input("How many years have you been a resident in the U.S. ? "))
    if time_in_US < 14:
        print("I am sorry, you have be a resident in the U.S. for at least 14 years ")
    else:
        age = int(input("How old are you? "))
        if age < 35:
            print("I am sorry, you are not old enough to be president. Maybe try again in a few years!")
        else:
            print("Yay you are eligible to be president! Now, go campaign!")
else:
    print("I am sorry, you are not eligible to be president. You have to be born in the U.S.")
