#!/usr/bin/env python3
def famous_births(figures):
    sorted_birthdate = sorted (figures.items(), key=lambda items: items[1]["date_of_birth"])
    for key,info in sorted_birthdate:
        print(f"{info["name"]} is a great scientist born in {info["date_of_birth"]}")
def main():
    women_scientists = {
    "ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
    "cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
    "lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
    "grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
    }
    famous_births(women_scientists)

if __name__ == "__main__":
    main() 