def main():
	print("This program subtracts two numbers.")
	num1 = input("Enter first number: ")
	num1 = int(num1)
	num2 = input("Enter second number: ")
	num2 = int(num2)
	diff = num1 - num2
    
	print("The difference is " + str(diff) + ".")

if __name__ == '__main__':
    main()