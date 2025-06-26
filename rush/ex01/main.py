#!/usr/bin/env python3
import sys
from checkmate import checkmate

def main():
    if len(sys.argv) < 2:
        print("Error")
        return

    for filename in sys.argv[1:]:
        try:
            with open(filename, 'r') as file:
                board = file.read().strip()
                result = checkmate(board)
                print(result)
        except FileNotFoundError:
            print("Error")
        except Exception:
            print("Error")

if __name__ == "__main__":
    main()
