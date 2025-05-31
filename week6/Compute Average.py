def main():
    number_list = load_numbers_from_file("numbers.txt")

    if len(number_list) > 0:
        average = sum(number_list) / len(number_list) 
        print("Average:", average) 
    else:
        print("The list is empty. Cannot compute average.")


def load_numbers_from_file(filepath):
    numbers = []
    with open(filepath, 'r') as file_reader:
        for line in file_reader.readlines():
            cleaned_line = line.strip()
            if cleaned_line != '':
                numbers.append(float(cleaned_line))  
    return numbers


if __name__ == '__main__':
    main()

