#!/usr/bin/env python3
import sys

from pathlib import Path

def checkmate(bd_str):
    bd = bd_str.splitlines()
    sz = len(bd)

    if any(len(row) != sz for row in bd):
        return "Error"

    kp = None
    for x in range(sz):
        for y in range(sz):
            if bd[x][y] == 'K':
                kp = (x, y)
                break
        if kp:
            break

    if not kp:
        return "Error"

    kx, ky = kp

    def ib(x, y):
        return 0 <= x < sz and 0 <= y < sz

    def cd(dx, dy, atk):
        x, y = kx + dx, ky + dy
        while ib(x, y):
            pc = bd[x][y]
            if pc != '.':
                return pc in atk
            x += dx
            y += dy
        return False

    def cp():
        pa = [(1, -1), (1, 1)]
        for dx, dy in pa:
            x, y = kx + dx, ky + dy
            if ib(x, y) and bd[x][y] == 'P':
                return True
        return False

    def ck():
        km = [
            (-2, -1), (-2, 1), (-1, -2), (-1, 2),
            (1, -2), (1, 2), (2, -1), (2, 1)
        ]
        for dx, dy in km:
            x, y = kx + dx, ky + dy
            if ib(x, y) and bd[x][y] == 'N':
                return True
        return False

    if cd(0, 1, 'RQ') or cd(0, -1, 'RQ') or cd(1, 0, 'RQ') or cd(-1, 0, 'RQ'):
        return "Success"

    if cd(1, 1, 'BQ') or cd(1, -1, 'BQ') or cd(-1, 1, 'BQ') or cd(-1, -1, 'BQ'):
        return "Success"

    if cp():
        return "Success"

    if ck():
        return "Success"

    return "Fail"

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 main.py board1.chess [board2.chess ...]")
        sys.exit(1)

    for file in sys.argv[1:]:
        try:
            with open(file, "r") as f:
                board_data = f.read()
                result = checkmate(board_data)
                print(result)
        except Exception:
            print("Error")
