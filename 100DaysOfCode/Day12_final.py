#NUMBER GUESSING GAME

'''
Computer chooses one number randomly between 1 and 100 we should guess it
we can select Easy and Hard level
in Easy we get 10 chances and Hard 5 chances
everytime if answer is wrong computer says, our guess is high or low'''
from random import randint

'''def computer_guess():
    return randint(1,100)'''

computers_choice=randint(1,100)

print("Welcome to Number Guessing Game \nI'm Guessing a number between 1 and 100.")

def mode_choices():
    mode=input("Choose a Difficulty, Types 'EASY' or 'Difficult'\n").lower()
    if mode=="easy":
      print("You now have 10 chances to guess the correct Number")
      return 10
    elif mode=="difficult":
      print("You now have 5 chances to guess the correct Number")
      return 5
    else:
      print("you entered something wrong")

choises=mode_choices()
while choises>0:
    user_choice=int(input("Enter your guess number between 1 and 100 \n"))
    if user_choice>computers_choice:
        choises-=1
        print(f"Too High, you have {choises} chances left")
        if choises==0:
          continue_game=input("Do you want to continue the game? if types 'yes' or 'no' \n").lower()
          if continue_game=='yes':
            choises=mode_choices()
    elif user_choice<computers_choice:
        choises-=1
        print(f"Too Low, you have {choises} chances left")
        if choises==0:
          continue_game=input("Do you want to continue the game? if types 'yes' or 'no' \n").lower()
          if continue_game=='yes':
            choises=mode_choices()
    elif user_choice==computers_choice:
        choises-=1
        print(f"Correct Answer, huhu you did it with {choises} chances left")
        continue_game=input("Do you want to continue the game? if types 'yes' or 'no' \n").lower()
        if continue_game=='yes':
          choises=mode_choices()
        else:
          break