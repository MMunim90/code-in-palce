from karel.stanfordkarel import *

def main():
    """
    Karel starts facing East in the bottom left corner of the world and ends facing East in the bottom right corner of the world.
    """
    turn_left()
    moving()
    turn_right()
    moving()
    turn_right()
    moving()
    turn_left()

def moving():
    move()
    move()
    move()

def turn_right():
    turn_left()
    turn_left()
    turn_left()



# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()