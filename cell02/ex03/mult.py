try:
    a = float(input("Enter first number:\n"))
    b = float(input("Enter second number:\n"))
    result = a * b
    print(f"{a} x {b} = {result}")

    if result > 0:
        print("The result is positive.")
    elif result < 0:
        print("The result is negative.")
    else:
        print("The result is potive and negative.")

except ValueError:
    print("Invalid input. Please enter a Real number.")