from karel.stanfordkarel import *

def main():

    for i in range(4):
        putting_beepers()
        moving()


def putting_beepers():
    put_beeper()
    move()
    put_beeper()
    turn_left()
    move()
    put_beeper()


def moving():
    turn_right()
    move()
    turn_left()
    if front_is_clear():
        move()
        move()


def turn_right():
    for i in range(2):
        turn_left()
    
if __name__ == '__main__':
    main()