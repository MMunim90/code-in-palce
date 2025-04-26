from karel.stanfordkarel import *

def main():
    while front_is_clear():
        if beepers_present():
            move()
        else:
            turn_right()
    turn_left()

def turn_right():
    for i in range(3):
        turn_left()


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()