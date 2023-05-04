"""
File: DoubleBeepers.py
Name:KaiYing Cheng
-------------------------------
TODO:
"""

from karel.stanfordkarel import *


def turn_around():
    turn_left()
    turn_left()


def main():
    move()
    double_beeper()
    move()
    while on_beeper():
        pick_beeper()
        turn_around()
        move()
        put_beeper()
        turn_around()
        move()
    turn_around()
    while front_is_clear():
        move()
    turn_around()


def double_beeper():
    while on_beeper():
        pick_beeper()
        move()
        put_beeper()
        put_beeper()
        turn_around()
        move()
        turn_around()



# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
