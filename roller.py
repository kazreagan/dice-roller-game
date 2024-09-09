import random

#create a function to roll the dice
def roll_dice():
    return random.randint(1, 6)

#create a loop to allow multiple rolls
while True:
    roll = input("Roll the dice? (Y/n): ")
    if roll == "Y":
        print(f"you rolled a {roll_dice()}!")

    elif roll == "n":
        print("Goodbye!")
        break
    else:
        print("Invalid Input!")