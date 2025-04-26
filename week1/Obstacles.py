from karel.stanfordkarel import *

def main():
    """
    Karel starts facing East in the bottom left corner of the world and ends facing East in the bottom right corner of the world.
    """
    move()
    turn_left()
    putting_beeper()
    turn_right()
    move()
    move()

def putting_beeper():
    for i in range(3):
        move()
        put_bep()


def put_bep():
    turn_right()
    move()
    put()
    

def put():
    turn_right()
    move()
    put_beeper()
    turn_left()
    turn_left()


def turn_right():
    turn_left()
    turn_left()
    turn_left()


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()