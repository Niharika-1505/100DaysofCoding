def jump_hurdle():
    move()
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


def turn_down():
    turn_left()
    turn_left()


no_of_hurdles = 6
while no_of_hurdles > 0:
    jump_hurdle()
    no_of_hurdles -= 1

################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
