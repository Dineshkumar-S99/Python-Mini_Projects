#Makde way for the bot

#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json

val=6
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def one_movement():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
while val>0:
    one_movement()
    val-=1