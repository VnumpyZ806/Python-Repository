def move_right():
    turn_left()
    turn_left()
    turn_left()
    
def move_through_hurdle():
    move()
    turn_left()
    move()
    move_right()
    move()
    move_right()
    move()
    turn_left()
    
number_of_hurdles = 6
while at_goal() != True:
    move_through_hurdle()
