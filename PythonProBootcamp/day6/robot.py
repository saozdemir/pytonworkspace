"""
 @author saozdemir
 @project PycharmProjects robot
 @date 02 Eki 2026
 <p>
 @description:
"""


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


for step in range(6):
    jump()

###########
def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    turn_left()
    while not right_is_clear():
        move()
    turn_right()
    move()
    turn_right()
    while not wall_in_front():
        move()
    turn_left()


while not at_goal():
    if not front_is_clear():
        jump()
    else:
        move()
