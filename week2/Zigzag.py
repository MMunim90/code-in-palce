from karel.stanfordkarel import *

def main():
    """
    Places beepers in a zig zag pattern.
    """
    #print_up()
    #put_the_beeper()
    #print_down()
    
    while front_is_clear():
        put_beeper()
        print_up()
        put_beeper()
        print_down()
        

def print_up():
    turn_left()
    move()
    turn_right()
    move()

def print_down():
    turn_right()
    move()
    turn_left()
    if front_is_clear():
        move()

def turn_right():
    for i in range(3):
        turn_left()


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()