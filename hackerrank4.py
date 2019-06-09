import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):

    countPostives = 0
    countNegatives = 0
    countZeros = 0
    for number in arr:
        if number > 0:
            countPostives += 1
        if number < 0:
            countNegatives += 1
        if number == 0:
            countZeros += 1
    postive_fractions = countPostives / len(arr)
    negative_fractions = countNegatives / len(arr)
    zero_fractions = countZeros / len(arr)

    #print(f"{str(postive_fractions)} for postive and {str(negative_fractions)} "
     #     f"for negatives and {str(zero_fractions)} for zero guys ")
    print(postive_fractions)
    print(negative_fractions)
    print(zero_fractions)



if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)