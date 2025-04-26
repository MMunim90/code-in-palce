from karel.stanfordkarel import *

def main():
    """
    Makes Karel place beepers in a square (4 beepers total) and end in the same position Karel starts in.
    """
    
    for i in range(4):
        move()
        put_beeper()
        turn_left()


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()