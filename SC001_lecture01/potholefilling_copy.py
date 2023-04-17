"""
File: PotholeFilling.py
Name: KaiYing Cheng
--------------------------
This program shows karel filling 3
potholes. Students learn the concept of
decomposition through the process.
"""

from karel.stanfordkarel import *


def turn_around():
    turn_left()
    turn_left()


def turn_right():
    for i in range(3):
        turn_left()


def put_99_beepers():
    for i in range(99):
        put_beeper()


def go_in():
    """
    pre-condition:Karel is at the upper left of the pot hole, facing East
    post-condition:Karel is in the pothole, facing South
    """
    move()
    turn_right()
    move()


def go_out():
    """
    pre-condition:Karel is in the pothole, facing South
    post-condition:Karel is at the upper left of the pot hole, facing East
    """
    turn_around()
    move()
    turn_right()
    move()


def anti_go_in():
    move()
    turn_left()
    move()


def anti_go_out():
    turn_around()
    move()
    turn_left()
    move()


def pick_99_beepers():
    for i in range(99):
        pick_beeper()

def main():
    for i in range(3):
        go_in()
        put_99_beepers()
        go_out()
    turn_around()
    for i in range(3):
        anti_go_in()
        pick_99_beepers()
        anti_go_out()
    turn_around()




# ----- DO NOT EDIT CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
