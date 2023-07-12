from random import randint
user_choice = int(input("What do you choose? type 0 for Rock, 1 for Paper, 2 for Scissor "))

item = ["Rock", "Paper", "Scissor"]

computer_choice = randint(0, 2)
print(f"You choose {item[user_choice]}")
print(f"Computer choose {item[computer_choice]}")

if user_choice == 0 and computer_choice == 2:
    print("user win")
elif user_choice == 2 and computer_choice == 1:
    print("user win")
elif user_choice == 1 and computer_choice == 0:
    print("user win")
elif user_choice == computer_choice:
    print("It is a Draw")
else:
    print("computer win")
    
    