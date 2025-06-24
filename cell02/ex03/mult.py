try:
    a = float(input("Enter first number:\n"))
    if a == 0:
        print("The result is potive and negative.")
    else:
        b = float(input("Enter second number:\n"))
        if b == 0:
            print("The result is potive and negative.")
        else:
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