#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the pylons function below.
def pylons(k, arr):

    i, j, loc, ret = 0, 0, 0, 0
    cant = False

    while i < len(arr):
        ret += 1
        j = i + k - 1
        if j > n: j = n - 1
        while loc <= j < n and arr[j] == 0: j -= 1

        if j < loc:
            cant = True
            return -1

        loc = j + 1
        j = j + k
        i = j
    if not cant: return ret

    

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = pylons(k, arr)


    print(result)
    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
