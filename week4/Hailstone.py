def main():
    n = int(input("Enter a number: "))
    steps = 0

    while n != 1:
        if n % 2 == 0:
            # Even case
            print(f"{n} is even, so I take half: {int(n / 2)}")
            n = int(n / 2)
        else:
            # Odd case
            print(f"{n} is odd, so I make 3n + 1: {3 * n + 1}")
            n = 3 * n + 1
        steps += 1


if __name__ == "__main__":
    main()
