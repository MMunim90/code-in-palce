from karel.stanfordkarel import *

def main(): 

    front_clear()
    for i in range(2):
        move_forword()
    turn_right()


def move_forword():
    while right_is_blocked(): 
        if front_is_clear():
            move()
    make_flower()
    for i in range(2):
        clearly_moving()


def front_clear():
    if front_is_clear():
        move()
        turn_left()

def clearly_moving():
        while front_is_clear():
            move()
        turn_left()


def make_flower():
    put_beeper()
    move()
    for i in range(2):
        put_beeper()
        turn_right()
        move()
    put_beeper()


def turn_right():
    for i in range(3):
        turn_left()


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()