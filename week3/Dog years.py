DOG_YEARS_MULTIPLIER = 7.18  

def main():
    dog_age = int(input("Enter an age in calendar years: "))
    total_age = dog_age * DOG_YEARS_MULTIPLIER
    print("That's", total_age, "in dog years!") 

if __name__ == '__main__':
    main()