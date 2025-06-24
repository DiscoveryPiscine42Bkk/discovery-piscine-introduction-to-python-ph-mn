try:
    num = float(input())
    if num > 0:
        print("This number is positive.")
    elif num < 0:
        print("This number is negtive.")
    else:
        print("This number is both potive and negative.")
except ValueError:
    print("Invalid input. Please enter a number.")