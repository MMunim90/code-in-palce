from karel.stanfordkarel import *

def main():
    
    while front_is_clear():
        getting_up()
        move()
        getting_down()
        if front_is_clear():
            move_forword()

def getting_up():
    turn_left()
    put_and_move()
    put_beeper()
    turn_right()

def getting_down():
    turn_right()
    put_and_move()
    put_beeper()
    turn_left()

def put_and_move():
    while front_is_clear():
        put_beeper()
        move()

def move_forword():
    for i in range(4):
        move()

def turn_right():
    for i in range(3):
        turn_left()


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()