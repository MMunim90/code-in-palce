from karel.stanfordkarel import *

def main():
    
    while beepers_present():
        moving()
        pick_beeper()
        move()
        turning_and_moving()
        moving()
        move_five_times()
        pick_beeper()
        turn_right()
        move()

def moving():
    for i in range(2):
        move_two_times()
        turn_left()

def turning_and_moving():
    turn_right()
    move_two_times()
    turn_right()
    move_five_times()
    turn_right()

def move_five_times():
    for i in range(5):
        pick_beeper()
        move()

def move_two_times():
    for i in range(2):
        pick_beeper()
        move()

def turn_right():
    for i in range(3):
        turn_left()


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()