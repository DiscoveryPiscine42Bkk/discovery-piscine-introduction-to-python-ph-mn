try:
    num1 = float(input("Enter the first number: \n"))
    num2 = float(input("Enter the second number: \n"))
    mult = num1 * num2
    print (num1, "x", num2, "=", mult)

    if mult > 0:
        print("This number is positive.")
    elif mult < 0:
        print("This number is negtive.")
    else:
        print("This number is both potive and negative.")

except ValueError:
    print("Invalid input. Please enter a Real number.")