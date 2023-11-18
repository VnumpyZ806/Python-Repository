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

for i in range(6):
    move_through_hurdle()
