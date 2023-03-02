#!/usr/bin/python3
'''
Module that solves the N Queens puzzle
'''

from sys import argv, exit
from typing import List



if __name__ == "__main__":
    if len(argv) != 2:
        print('Usage: nqueens N')
        exit(1)
    try:
        n = int(argv[1])
    except BaseException:
        print('N must be a number')
        exit(1)
    if n < 4:
        print('N must be at least 4')
        exit(1)

    reslt: List = list()

    def solve_queens(row, n, reslt):
        if (row == n):
            print(reslt)
        else:
            for col in range(n):
                placement = [row, col]
                if valid_placement(reslt, placement):
                    reslt.append(placement)
                    solve_queens(row + 1, n, reslt)
                    reslt.remove(placement)

    def valid_placement(reslt, placement):
        for queen in reslt:
            if queen[1] == placement[1]:
                return False
            if (queen[0] + queen[1]) == (placement[0] + placement[1]):
                return False
            if (queen[0] - queen[1]) == (placement[0] - placement[1]):
                return False
        return True

    solve_queens(0, n, reslt)