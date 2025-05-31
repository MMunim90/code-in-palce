def find_karel(roster):
    if 'karel' in roster:
        print("Karel is here!")
    else:
        print("Karel isn't here.")


def get_list():
    lst = []
    elem = input("Please enter an element of the list or press enter to stop. ")
    while elem != "":
        lst.append(elem.lower())
        elem = input("Please enter an element of the list or press enter to stop. ")
    return lst

def main():
    roster = get_list()
    find_karel(roster)


if __name__ == '__main__':
    main()