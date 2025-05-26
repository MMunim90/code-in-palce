def main():
    print("Enter a sequence of non-decreasing numbers.")

    count = 0  
    prev = None  

    while True:
        num = float(input("Enter num: ")) 

        if prev is None:
            prev = num
            count += 1
        elif num >= prev:
            prev = num
            count += 1
        else:
            break

    print("Thanks for playing!")
    print("Sequence length:", count)

if __name__ == "__main__":
    main()