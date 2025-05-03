from karel.stanfordkarel import *

def main():

    while front_is_clear():
        while front_is_clear():
            put_beeper()
            move()
        put_beeper()
        u_turn()
        moving_freely()
        turn_right()
        if front_is_clear():
            move()
            turn_right()
    turn_right()
    moving_freely()

def moving_freely():
    while front_is_clear():
        move()
   
def turn_right():
    for i in range(3):
        turn_left()

def u_turn():
    for i in range(2):
        turn_left()
    


# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()


# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()