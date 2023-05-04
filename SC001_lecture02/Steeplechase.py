"""
File: Steeplechase.py
Name: KaiYing Cheng
---------------------------------
TODO:
"""

from karel.stanfordkarel import *


def main():
    for i in range(11):
        if front_is_clear():
            move()
        else:
            jump()
            turn_left()


def turn_right():
    for i in range(3):
        turn_left()


def jump():
    """
    Pre-condition:Karel is on the left, facing East
    Post-condition:Karel is on the right
    """
    up()
    cross()
    down()


def up():
    """
    Pre-condition:Karel is on the right
    Post-condition:Karel in on the peak
    """
    while not front_is_clear():
        turn_left()
        move()
        turn_right()


def cross():
    """
    Pre-condition:Karel is on the right side of the peak,facing East
    Post_condition:Karel is on the left side of the peak,facing West
    """
    while front_is_clear():
        move()
        turn_right()


def down():
    """
    Pre-condition:Karel is on the left side of the peak,facing West
    Post_condition:Karel is on the left, facing East
    """
    turn_left()
    while front_is_clear():
        move()



# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
