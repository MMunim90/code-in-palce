from karel.stanfordkarel import *

def main():
    """
    Fills entire bottom row of any sized world with beepers.
    """
    put_beeper()
    #put_many_beepers()
    while front_is_clear():
        move()
        put_many_beepers()


def put_many_beepers():
    for i in range(1):
        put_beeper()


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()