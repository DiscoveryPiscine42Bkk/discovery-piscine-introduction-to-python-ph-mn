import sys
from checkmate import checkmate

def main():
    if len(sys.argv) < 2:
        print('None')
        exit()
    for filename in sys.argv[1:]:
        with open(filename, 'r') as f:
            board = f.read()
            checkmate(board)
























if __name__ == "__main__":
    main()