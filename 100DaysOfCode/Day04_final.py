rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

game = [rock, paper, scissors]

user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
print(f"you chose:\n{game[user_input]}")

computer_chose =random.randint(0,2)
print(f"computer chose:\n{game[computer_chose]}")

if user_input == computer_chose:
    print("It's a tie!")
elif user_input == 0 and computer_chose == 1:
      print("You lose!")
elif user_input == 1 and computer_chose == 2:
      print("You lose!")
elif user_input == 2 and computer_chose == 0:
      print("You lose!")
else:
      print("You win!")

