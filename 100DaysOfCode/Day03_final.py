#to make a tressure island game with if else classes 

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

left_right=input("which Direction would you like to choose type 'left' or 'right' : \n").lower()
if left_right == "right":
    print("Oops! you met with an accident .. \nGame Over!")
elif left_right =="left":
    swim_wait = input("reached next level and you're in a lake choose 'swim' or 'wait' : \n").lower()
    if swim_wait == "swim":
        print("Opps! you got attacked by Gladiators and Pranafishes...\n Game Over!! ")
    elif swim_wait =="wait":
        door_color =input("huhu you got a boat and came to Treasure Island \n now last step there are three Doors choose one \n to choose one type Red , Blue or Yellow : \n ").lower()
        if door_color =="red":
            print("Alass! you got burned it's a fire Door :! \n Game Over!!")
        elif door_color =="blue":
            print("Hurreyyy ! you Got the Tressure and won the Game ^_^ ")
        elif door_color =="yellow":
            print("you got into the hands of Beast :(  \n Game Over!!")
else:
    print("You Typed a wrong Keyword :! \n Game Over!!")

