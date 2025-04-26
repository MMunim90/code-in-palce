from karel.stanfordkarel import *

# Here is a place to program your Section problem

def main():

    while front_is_clear():
        move()
        if beepers_present():
            build_hospital()
    
def build_hospital():
    turn_left()
    move()
    put_beeper()
    move()
    put_beeper()
    turn_right()
    move()
    put_beeper()
    turn_right()
    move()
    put_beeper()
    move()
    put_beeper()
    turn_left()

def turn_right():
    for i in range(3):
        turn_left()

if __name__ == '__main__':
    main()