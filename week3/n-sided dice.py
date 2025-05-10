import random

def main():
    num_sides = int(input("How many sides does your dice have? ")) 
    dice = random.randint(1, num_sides)
    print(f"Your roll is {dice}")
if __name__ == '__main__':
    main()