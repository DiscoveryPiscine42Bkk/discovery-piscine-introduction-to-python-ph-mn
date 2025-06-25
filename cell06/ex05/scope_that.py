#!/usr/bin/env python3
def add_one(num):
    num += 1

number = 10
print("Number before the call:", number)
add_one(number)
print("Number after the call:", number)

#Even though we changed the value in the function, 
#it does not affect the variable that was paseed into the function.