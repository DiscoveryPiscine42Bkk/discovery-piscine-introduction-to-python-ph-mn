try:
    import math

    number = float(input("Enter a number: "))
    print(math.ceil(number))
    
except ValueError:
    print("Invalid input. Please enter a numeric value.")