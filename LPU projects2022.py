import random

print("Welcome to DICE GAME!")

i = ""
scr = 0

while i != "n":
    x = int(input("Enter Number from (1-6): "))
    y = random.randint(1, 6)
    if x not in range(1, 6 + 1):
        print("Number must be between 1 to 6!")
    else:
        print(x, y)
        if x == y:
            scr += 5
    i = str(input("Do you want to continue? (Y/n): "))

print("Game Exited!")
print("Your Score:", scr)
