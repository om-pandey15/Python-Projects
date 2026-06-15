import random
item_list =["Rock","Paper","Scissors"]

user_choice = input("Enter your move(Rock, Paper, Scissors): ")
comp_choice = random.choice(item_list)

print(f"Your choice: {user_choice}")
print(f"Computer's choice: {comp_choice}")

if user_choice == comp_choice:
    print("Both choose the same: = Match tie")

elif user_choice == "Rock":
    if comp_choice == "Scissors":
        print("You win!")
    else:
        print("Computer wins!")
elif user_choice == "Paper":
    if comp_choice == "Rock":
        print("You win!")
    else:
        print("Computer wins!")
elif user_choice == "Scissors":
    if comp_choice == "Paper":
        print("You win!")
    else:
        print("Computer wins!")