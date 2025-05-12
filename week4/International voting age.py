PETURKSBOUIPO_AGE = 16
STANLAU_AGE = 25
MAYENGUA_AGE = 48

def main():
    age = int(input("How old are you? "))

    if(age > PETURKSBOUIPO_AGE):
        print("You can vote in Peturksbouipo where the voting age is 16.")
    else:
        print("You cannot vote in Peturksbouipo where the voting age is 16.")

    if(age > STANLAU_AGE):
        print("You can vote in Stanlau where the voting age is 25.")
    else:
        print("You cannot vote in Stanlau where the voting age is 25.")

    if(age > MAYENGUA_AGE):
        print("You can vote in Mayengua where the voting age is 48.")
    else:
        print("You cannot vote in Mayengua where the voting age is 48.")

if __name__ == '__main__':
    main()