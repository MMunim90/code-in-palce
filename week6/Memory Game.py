import random

NUM_PAIRS = 3

def main():
    truth_list = create_truth_list(NUM_PAIRS)
    random.shuffle(truth_list)

    displayed_list = ['*'] * len(truth_list)

    while '*' in displayed_list:
        print(displayed_list)
        index1 = get_valid_index(displayed_list, None)
        index2 = get_valid_index(displayed_list, index1)

        if truth_list[index1] == truth_list[index2]:
            displayed_list[index1] = truth_list[index1]
            displayed_list[index2] = truth_list[index2]
            print("Match!")
        else:
            print(f"Value at index {index1} is {truth_list[index1]}")
            print(f"Value at index {index2} is {truth_list[index2]}")
            print("No match. Try again.")
            input("Press Enter to continue...")

        clear_terminal()

    print(displayed_list)
    print("Congratulations! You won!")

def create_truth_list(num_pairs):
    truth = []
    for i in range(num_pairs):
        truth.append(i)
        truth.append(i)
    return truth

def get_valid_index(displayed_list, first_index):
    while True:
        inp = input("Enter an index: ")
        if not inp.isdigit():
            print("Not a number. Try again.")
            continue

        index = int(inp)

        if index < 0 or index >= len(displayed_list):
            print("Invalid index. Try again.")
            continue

        if displayed_list[index] != '*':
            print("This number has already been matched. Try again.")
            continue

        if first_index is not None and index == first_index:
            print("You entered the same index twice. Try again.")
            continue

        return index

def clear_terminal():
    for _ in range(20):
        print('\n')

if __name__ == '__main__':
    main()
