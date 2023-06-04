#BLACK JACK
from random import randint

#if A -> default value is 11 and if above 21 it can be set as 1, and K,Q,J values are equal to 10
Ace=11
King,Queen,Jack=10,10,10

#print(K,Q,J)
cards=[Ace,2,3,4,5,6,7,8,9,10,King,Queen,Jack]
users_value=[]
computers_value=[]

def first_choices(cards,users_value,computers_value):
    value=2
    while value>0:
        users_value.append(cards[randint(0,len(cards)-1)])
        computers_value.append(cards[randint(0,len(cards)-1)])
        value-=1
    return users_value,computers_value

def adding_vals(values):
    total=0
    for val in values:
        total+=val
    return total     

users_total=0
computers_total=0
def blackjack_first(cards,users_value,computers_value,users_total,computers_total):
    first_choices(cards,users_value,computers_value)
    users_total=adding_vals(users_value)
    computers_total=adding_vals(computers_value)
    print(f"Your cards are {users_value} and your total is {users_total}")
    return computers_total,users_total

#blackjack_first(cards,users_value,computers_value,users_total,computers_total)

def ace():
    if Ace in users_value and users_total>21:
        users_value.remove(Ace)
        Ace=1
        users_value.append(Ace)
        return adding_vals(users_value)


game_play=True

while game_play:
    play_game=input("Do you want to start the game? \nTypes 'Y' for Yes and 'N' for no: ").lower()
    if play_game=="y":
        ace()
        blackjack_first(cards,users_value,computers_value,users_total,computers_total)
        play_game=input("Do you want to change the card? \nTypes 'Y' for Yes and 'N' for no: ").lower()
        if play_game=="y":
            users_thirdcard=cards[randint(0,len(cards)-1)]
            #computers_thirdcard=cards[randint(0,len(cards)-1)]
            users_value.append(cards[randint(0,len(cards)-1)])
            users_total+=users_thirdcard
            #computers_total+=computers_thirdcard
            ace()
            if users_total>21:
                print("You lose")
                game_play=input("Do you want to play again? \nTypes 'Y' for Yes and 'N' for no: ").lower()
                if game_play=="y":
                    continue
                else:
                    break
            elif computers_total==21 or computers_total>users_total:
                print("You lose")
                game_play=input("Do you want to play again? \nTypes 'Y' for Yes and 'N' for no: ").lower()
                if game_play=="y":
                    continue
                else:
                    break
            elif computers_total<17:
                computers_thirdcard=cards[randint(0,len(cards)-1)]
                computers_total+=computers_thirdcard
                if computers_total==21 or computers_total>users_total:
                  print("You lose")
                  game_play=input("Do you want to play again? \nTypes 'Y' for Yes and 'N' for no: ").lower()
                  if game_play=="y":
                    continue
                  else:
                    break
                elif computers_total==users_total:
                    print("It's a Draw!")
                    game_play=input("Do you want to play again? \nTypes 'Y' for Yes and 'N' for no: ").lower()
                    if game_play=="y":
                      continue
                    else:
                      break
                else:
                    print("You win!!!!")
                    game_play=input("Do you want to play again? \nTypes 'Y' for Yes and 'N' for no: ").lower()
                    if game_play=="y":
                      continue
                    else:
                      break
            elif computers_total==users_total:
                print("It's a Draw!")
                game_play=input("Do you want to play again? \nTypes 'Y' for Yes and 'N' for no: ").lower()
                if game_play=="y":
                  continue
                else:
                  break
            else:
              print("You win!!!!")
              game_play=input("Do you want to play again? \nTypes 'Y' for Yes and 'N' for no: ").lower()
              if game_play=="y":
                continue
              else:
                break
        elif play_game=="n":
          if users_total>21:
            print("You lose")
            game_play=input("Do you want to play again? \nTypes 'Y' for Yes and 'N' for no: ").lower()
            if game_play=="y":
              continue
            else:
              break
          elif computers_total==21 or computers_total>users_total:
            print("You lose")
            game_play=input("Do you want to play again? \nTypes 'Y' for Yes and 'N' for no: ").lower()
            if game_play=="y":
              continue
            else:
              break
          elif computers_total<17:
            computers_thirdcard=cards[randint(0,len(cards)-1)]
            computers_total+=computers_thirdcard
            if computers_total==21 or computers_total>users_total:
              print("You lose")
              game_play=input("Do you want to play again? \nTypes 'Y' for Yes and 'N' for no: ").lower()
              if game_play=="y":
                continue
              else:
                break
            elif computers_total==users_total:
              print("It's a Draw!")
              game_play=input("Do you want to play again? \nTypes 'Y' for Yes and 'N' for no: ").lower()
              if game_play=="y":
                continue
              else:
                break
            else:
              print("You win!!!!")
              game_play=input("Do you want to play again? \nTypes 'Y' for Yes and 'N' for no: ").lower()
              if game_play=="y":
                continue
              else:
                break
          elif computers_total==users_total:
            print("It's a Draw!")
            game_play=input("Do you want to play again? \nTypes 'Y' for Yes and 'N' for no: ").lower()
            if game_play=="y":
              continue
            else:
              break
          else:
            print("You win!!!!")
            game_play=input("Do you want to play again? \nTypes 'Y' for Yes and 'N' for no: ").lower()
            if game_play=="y":
              continue
            else:
              break
        else:
          print("You have entered a wrong value")
          continue
    else:
       break
                
    
#print(cards[0],cards[-2])