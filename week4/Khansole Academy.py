import random

"""
CORRECT_THREE_TIMES = 3
def main():
    print("Khansole Academy")
    correct_count = 0
    
    while correct_count < CORRECT_THREE_TIMES:
        num1 = random.randint(10, 99)
        num2 = random.randint(10, 99)

        print(f"What is {num1} + {num2}?")
        answer = int(input("Your answer: "))  

        total = num1 + num2
        if answer == total:
            print("Correct!")
            correct_count += 1
            print(f"You've gotten {correct_count} correct in a row. ")
        else:
            print("Incorrect.")
            print(f"The expected answer is {total}")
            correct_count = 0
        
        if correct_count == 3:
            print("Congratulations! You mastered addition.")


"""

def main():
    print("Khansole Academy")
    
    num1 = random.randint(10, 99)
    num2 = random.randint(10, 99)

    print(f"What is {num1} + {num2}?")
    answer = int(input("Your answer: "))  

    total = num1 + num2
    if answer == total:
        print("Correct!")
    else:
        print("Incorrect.")
        print(f"The expected answer is {total}")
    
if __name__ == '__main__':
    main()