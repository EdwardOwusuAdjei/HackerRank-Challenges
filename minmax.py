import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    arr.sort()
    max_value = sum(arr[1:])
    min_value = sum(arr[0:4])
    print(f"{str(min_value)} {str(max_value)}")

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
