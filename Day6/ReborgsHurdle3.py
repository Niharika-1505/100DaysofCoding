def jump_hurdle():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


def turn_right():
    turn_left()
    turn_left()
    turn_left()


while at_goal() != True:
    if front_is_clear():
        move()
    elif wall_in_front():
        jump_hurdle()

################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
