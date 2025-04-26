from karel.stanfordkarel import *

# File: piles.py
# -----------------------------
# The warmup program defines a "main"
# function which should make Karel
# pick up all the beepers in the world.
def main():
    for i in range(3):
        move()
        pick_all_beeper()
        move()
    
   
def pick_all_beeper():
    for i in range(10):
        pick_beeper()
   
   
# don't edit these next two lines
# they tell python to run your main function
if __name__ == '__main__':
    main()