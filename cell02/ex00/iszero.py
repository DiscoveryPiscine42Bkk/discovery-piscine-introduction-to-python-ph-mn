try:
    n = float(input())
    if n == 0:
        print("This number is equal to zero.")
    else:
        print("This number is different from zero.")
except ValueError:
    print("Invalid input. Please enter a number.")