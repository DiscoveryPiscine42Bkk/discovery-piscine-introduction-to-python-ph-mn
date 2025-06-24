try:
    a = int(input("Give me your first: "))
    b = int(input("Give me your second: "))
    print("Thank you!")
    print(f"{a} + {b} = {a+b}")
    print(f"{a} - {b} = {a-b}")
    print(f"{a} / {b} = {a/b}")
    print(f"{a} x {b} = {a*b}")
except ValueError:
    print("Invalid input. Please enter a numeric value.")