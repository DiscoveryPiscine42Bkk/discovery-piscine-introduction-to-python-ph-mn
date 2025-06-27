#!/usr/bin/env python3
import sys
from checkmate import checkmate
from moveking import find_legal_moves

def main():
    if len(sys.argv) < 2:
        print('None')
        exit()
    try:
        for filename in sys.argv[1:]:
            with open(filename, 'r') as f:
                board = f.read()
                checkmate(board)
                find_legal_moves(board)
    except:
        print("\nError")
























if __name__ == "__main__":
    main()