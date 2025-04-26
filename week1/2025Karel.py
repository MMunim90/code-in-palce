from karel.stanfordkarel import *


def main():
   
    for i in range(20):
        put_beeper()
    move()
    for i in range(25):
        put_beeper()
    move()

if __name__ == '__main__':
    main()