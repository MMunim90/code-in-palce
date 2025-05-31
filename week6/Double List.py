def main():
    numbers = [1, 2, 3, 4] 

    for i in range(len(numbers)):  
        elem_at_index = numbers[i]  
        numbers[i] = elem_at_index * 2  

    print(numbers)  


if __name__ == '__main__':
    main()