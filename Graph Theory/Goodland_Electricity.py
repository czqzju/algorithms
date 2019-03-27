#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the pylons function below.
def pylons(k, arr):
    ret = 0
    cur = 0
    while cur < n:
        found = False
        for i in range(k - 1, 0, -1):
            if cur + i >=n: continue
            if arr[cur + i] == 1:
                found = True
                cur = cur + i
                ret += 1
                break
        if found == True:
            cur += k
        else:
            return -1
    return ret

    

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
