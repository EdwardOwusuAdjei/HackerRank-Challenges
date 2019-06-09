#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the compareTriplets function below.
def compareTriplets(a, b):
    countAlice = 0;
    countBob = 0;
    for alice, bob in zip(a, b):
        if(alice > bob):
            countAlice += 1
        if(bob > alice):
            countBob += 1
    return [countAlice,countBob]



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
