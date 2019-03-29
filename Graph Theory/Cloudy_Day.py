#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maximumPeople function below.
def maximumPeople(p, x, y, r):
    clouds = []
    for i in range(len(y)):
        lL = max(y[i] - r[i], 1)
        rL = y[i] + r[i]
        clouds.append([lL, rL])
    clouds.sort(key= lambda x: (x[0], x[1]))

    towns = {}
    for i in range(len(x)):
        if x[i] in towns: towns[x[i]] += p[i]
        else: towns[x[i]] = p[i]
    return 1

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = list(map(int, input().rstrip().split()))

    x = list(map(int, input().rstrip().split()))

    m = int(input())

    y = list(map(int, input().rstrip().split()))

    r = list(map(int, input().rstrip().split()))

    result = maximumPeople(p, x, y, r)

    print(result)

    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
