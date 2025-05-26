def main():
    height = float(input("Enter your height in meters: "))
    if(height > 1.6 and height < 1.9):  
        print('Correct height to be an astronaut')
    elif(height >= 1.9):
        print("Above maximum astronaut height")
    else:
        print("Below minimum astronaut height")
    
if __name__ == "__main__":
    main()