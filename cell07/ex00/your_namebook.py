#!/usr/bin/env python3
def array_of_names(names):
    full_names = []
    for first,last in names.items():
        fullname = f"{first.capitalize()} {last.capitalize()}"
        full_names.append(fullname)
    return full_names
def main():
    persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
    }
    print(array_of_names(persons))

if __name__ == "__main__":
    main() 