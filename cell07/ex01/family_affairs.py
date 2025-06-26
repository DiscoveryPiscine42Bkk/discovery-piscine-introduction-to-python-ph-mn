#!/usr/bin/env python3
def find_the_redheads(family_info):
    filtered = []
    redheads = {names: colors for names,colors in family_info.items() if colors == "red"}
    for names in redheads:
        filtered.append(names)
    return filtered
def main():
    dupont_family = {
    "florian": "red",
    "marie": "blond",
    "virginie": "brunette",
    "david": "red",
    "franck": "red"
    }
    print(find_the_redheads(dupont_family))

if __name__ == "__main__":
    main() 