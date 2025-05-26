MAX_NUMBER = 100

def main():
    for i in range(100):
        if((i+1) % 2 == 0):
            print(f"{i+1} is even")
        else:
            print(f"{i+1} is odd")

if __name__ == "__main__":
    main()