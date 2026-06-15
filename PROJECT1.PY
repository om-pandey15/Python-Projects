# We all have played snake,water gun game in our childhood.if you haven't, here's a simple implementation in Python:
#1 for snake
#-1 for water
#0 for gun
import random

computer = random.choice([-1, 0, 1])
youstr = input("Enter your choice: ")
youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "snake", -1: "water", 0: "gun"}

you = youDict[youstr]
#By now we have 2 number(variables) you and computer
print(f"You chose {reverseDict[you]} and computer chose {reverseDict[computer]}")

if(computer == you):
    print("It's a tie!")
elif (computer ==-1 and you == 1):
    print("You win!")
elif (computer == -1 and you == 0):
    print("You lose!")
elif (computer == 1 and you == -1):
    print("You win!")
elif (computer == 1 and you == 0):
    print("You lose!")
elif (computer == 0 and you == 1):
    print("You win!")
elif (computer == 0 and you == -1):
    print("You lose!")
else:
    print("It's a tie!")