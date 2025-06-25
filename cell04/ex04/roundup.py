try:
    import math

    n = float(input("Enter a number: "))
    print(math.ceil(n))

except ValueError:
    print("Invalid input. Please enter a numeric value.")