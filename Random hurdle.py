def move_right():
    turn_left()
    turn_left()
    turn_left()
    
def move_through_hurdle():  
    turn_left()
    move()
    move_right()
    move()
    move_right()
    move()
    turn_left()

while at_goal() != True:
    if front_is_clear():
        move()
    else:
        move_through_hurdle()
