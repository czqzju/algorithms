#!/bin/python3
#https://www.hackerrank.com/challenges/synchronous-shopping/problem
import math
import os
import random
import re
import sys

#
# Complete the 'shop' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. STRING_ARRAY centers
#  4. 2D_INTEGER_ARRAY roads
#

global a


def shop(n, k, centers, roads):
    global a
    INF = sys.maxsize
    dis = [[INF for _ in range(0, 2 ** k)] for _ in range(0, n)]
    edges = dict()
    for i in range(0, n):
        shopContents = centers[i].rstrip().split()
        for j in range(1, len(shopContents)):
            a[i] = a[i] | 1 << (int(shopContents[j]) - 1)

    for i in range(0, len(roads)):
        v1 = roads[i][0] - 1
        v2 = roads[i][1] - 1
        if v1 in edges: edges[v1][v2] = roads[i][2]
        else: edges[v1] = {v2 : roads[i][2]}
        if v2 in edges: edges[v2][v1] = roads[i][2]
        else: edges[v2] = {v1 : roads[i][2]}

    return 1


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    k = int(first_multiple_input[2])

    global a
    a = [0] * n

    centers = []

    for _ in range(n):
        centers_item = input()
        centers.append(centers_item)

    roads = []

    for _ in range(m):
        roads.append(list(map(int, input().rstrip().split())))

    res = shop(n, k, centers, roads)
    print(res)

    # fptr.write(str(res) + '\n')
    #
    # fptr.close()
