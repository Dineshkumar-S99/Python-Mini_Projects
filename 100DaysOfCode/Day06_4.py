#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json

#long method
def turn_right():
    turn_left()
    turn_left()
    turn_left()

    
while at_goal()!=True:
    if wall_in_front()==True:
        turn_left()
    else:
        move()
        turn_right()


#short

def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()

while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()