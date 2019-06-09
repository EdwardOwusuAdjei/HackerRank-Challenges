#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the diagonalDifference function below.
def diagonalDifference(arr):
    print(arr)
    first_diagonal = []
    second_diagonal = []
    count = 0
    for x in arr:
        first_diagonal.append(x[count])
        count += 1
    count = len(arr) - 1
    for x in arr:
        second_diagonal.append(x[count])
        count -= 1
    print(first_diagonal)
    print(second_diagonal)
    return abs(sum(first_diagonal) - sum(second_diagonal))


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)
    print(str(result))
    #fptr.write(str(result) + '\n')

    #fptr.close()
