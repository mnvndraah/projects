# This program is the solution of a test at:
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def check_move_right():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()

while not at_goal():
    while front_is_clear():
        move()
        check_move_right()
    while not front_is_clear():
        turn_left()
        if at_goal():
           break
        else:
            check_move_right()


# WORKS FOR ALL THE CASES GIVEN IN THE COURSE