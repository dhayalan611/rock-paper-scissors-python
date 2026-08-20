import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissor = """
   _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
game_icons = [rock, paper, scissor]

user_choice = int(input("Enter your choice: 0 for Rock, 1 for Paper, 2 for Scissor: "))
if user_choice >= 3 or user_choice < 0:
    print("Invalid choice")

else:
    print(game_icons[user_choice])
    computer_choice = random.randint(0,2)
    print("Computer choice: ")
    print(game_icons[computer_choice])

    if user_choice == computer_choice:
        print("Draw.")
    elif user_choice == 0 and computer_choice == 2:
        print("You won.")
    elif user_choice == 2 and computer_choice == 0:
        print("You lost.")
    elif computer_choice > user_choice:
        print("You lost.")
    elif user_choice > computer_choice:
        print("You won.")
