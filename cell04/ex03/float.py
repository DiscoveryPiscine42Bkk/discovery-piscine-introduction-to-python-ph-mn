try:
    n = float(input("Give me a number: "))

    if n.is_integer():
        print("This number is an integer.")
    else:
        print("This number is a decimal.")
except ValueError:
    print("Please enter a number.")