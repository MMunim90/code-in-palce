
from karel.stanfordkarel import *

def main():
    """
    Inverts the pattern of beepers in a single row world.
    """
    invert_corner()
    while front_is_clear():
        move()
        invert_corner()


def invert_corner():
    if beepers_present():
        pick_beeper()
    else:
        put_beeper()



# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()