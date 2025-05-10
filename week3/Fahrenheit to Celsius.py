def main():
    degrees_fahrenheit = float(input("Enter temperature in Fahrenheit: ")) 
    degrees_celsius = (degrees_fahrenheit - 32) * 5.0/9.0
    print("Temperature:", degrees_fahrenheit,"F =", degrees_celsius,"C")   

if __name__ == '__main__':
    main()