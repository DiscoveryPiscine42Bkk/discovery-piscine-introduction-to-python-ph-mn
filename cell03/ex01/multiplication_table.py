try:
    n = int(input("Enter a number:\n"))
    for i in range(10):
        print(f"{i} x {n} = {i * n}")

except ValueError:
    print("Please enter a Real number.")