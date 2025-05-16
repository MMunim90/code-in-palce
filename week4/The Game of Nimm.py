def main():
    TOTAL_STONES = 20
    
    while TOTAL_STONES > 0:
        print(f"There are {TOTAL_STONES} stones left.")
        removed1 = int(input("Player 1 would you like to remove 1 or 2 stones? "))
        while removed1 > 2:
            removed1 = int(input("Please enter 1 or 2: ")) 
        TOTAL_STONES = TOTAL_STONES - removed1
        if(TOTAL_STONES == 0):
            print("Player 2 wins!")
            return
        print("")
        if TOTAL_STONES > 0:
            print(f"There are {TOTAL_STONES} stones left.")
            removed2 = int(input("Player 2 would you like to remove 1 or 2 stones? "))
            while removed2 > 2:
                removed2 = int(input("Please enter 1 or 2: ")) 
            TOTAL_STONES = TOTAL_STONES - removed2
            if(TOTAL_STONES == 0):
                print("Player 1 wins!")
                return
            print("")

    if(removed1 > removed2):
        print("Player 1 wins!")
    elif(removed1 == removed2):
        print("Game over")
    else:
        print("Player 2 wins!")


if __name__ == '__main__':
    main()