from karel.stanfordkarel import *

def main():
    
    while front_is_clear():
        get_up()
        move_another_piller()
        get_down()
        if front_is_clear():
            move_another_piller()


def get_up():
    turn_left()
    moving_up_down()
    turn_right()

def get_down():
    turn_right()
    moving_up_down()
    turn_left()

def moving_up_down():
    for i in range(5):
        put_beeper()
        if front_is_clear():
            move()

def move_another_piller():
    for i in range(4):
        move()

def turn_right():
    for i in range(3):
        turn_left()

if __name__ == '__main__':
    main()