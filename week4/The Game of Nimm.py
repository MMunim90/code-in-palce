def main():
    TOTAL_STONES = 20
    
    while TOTAL_STONES > 0:
        print(f"There are {TOTAL_STONES} stones left.")
        removed1 = int(input("Player 1 would you like to remove 1 or 2 stones? "))
        if removed1 > 2:
            removed1 = int(input("Please enter 1 or 2: ")) 
        TOTAL_STONES = TOTAL_STONES - removed1
        print("")
        if TOTAL_STONES > 0:
            print(f"There are {TOTAL_STONES} stones left.")
            removed2 = int(input("Player 2 would you like to remove 1 or 2 stones? "))
            if removed2 > 2:
                removed2 = int(input("Please enter 1 or 2: ")) 
            TOTAL_STONES = TOTAL_STONES - removed2
            print("")

    if(removed1 > removed2):
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")
    #print("Game over")


if __name__ == '__main__':
    main()