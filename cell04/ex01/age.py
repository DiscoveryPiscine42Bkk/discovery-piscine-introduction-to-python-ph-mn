try:
    age = int(input("Please tell me your age: "))
    print("Your are currently", age, "year" if age == 1 else "years", "old")
    i = 10
    while i <= 30:
        print(f"In {i} years, you'll be {age+i} years old")
        i += 10

except ValueError():
    print("Please enter a number.")