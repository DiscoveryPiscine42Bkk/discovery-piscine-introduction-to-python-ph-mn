#!/usr/bin/env python3
def greetings(name = 'noble stranger'):
    if not isinstance(name,str):
        print("Error! It was not a name.")
    else:
        print("Hello,", name)

greetings('Alexander')
greetings("Wil")
greetings()
greetings(42)