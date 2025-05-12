AFFIRMATION = "I am capable of doing anything I put my mind to."

def main():
    print("Please type the following affirmation: I am capable of doing anything I put my mind to.")
    affirmation = input("")

    while affirmation != AFFIRMATION:
        if affirmation == AFFIRMATION:
            print("That's right! :)")
        else:
            print("That was not the affirmation.")
            
        print("Please type the following affirmation: I am capable of doing anything I put my mind to.")
        affirmation = input("")
    print("That's right! :)")  

if __name__ == '__main__':
    main()