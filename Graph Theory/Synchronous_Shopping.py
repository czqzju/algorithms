#!/bin/python3
#https://www.hackerrank.com/challenges/synchronous-shopping/problem
import math
import os
import random
import re
import sys
import heapq
from collections import OrderedDict
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

global a, distance, edges

def push(vn, vm, vv, s):
    global a, distance, edges
    if distance[vn][vm] <= vv: return
    distance[vn][vm] = vv
    s[(vn, vm)] = vv



if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    num = int(first_multiple_input[2])

    INF = sys.maxsize
    global a, distance, edges, s
    a = [0] * n
    distance = [[INF for _ in range(0, 2 ** num)] for _ in range(0, n)]
    edges = dict()
    # centers = []
    for i in range(n):
        shopContents = input().rstrip().split()
        for j in range(1, len(shopContents)):
            a[i] = a[i] | 1 << (int(shopContents[j]) - 1)




    for _ in range(m):
        roads = list(map(int, input().rstrip().split()))
        v1 = roads[0] - 1
        v2 = roads[1] - 1
        if v1 in edges:
            edges[v1][v2] = roads[2]
        else:
            edges[v1] = {v2: roads[2]}
        if v2 in edges:
            edges[v2][v1] = roads[2]
        else:
            edges[v2] = {v1: roads[2]}


    s = OrderedDict()
    push(0, a[0], 0, s)

    while len(s):
        (curNode, types), dis = s.popitem(last=False)
        for k, _ in edges[curNode].items():
            push(k, types | a[k], dis + edges[curNode][k], s)
    ret = INF

    for i in range(1, 1 << num):
        for j in range(i, 1 << num):
            if (i | j) == ((1 << num) - 1):
                ret = min(ret, max(distance[n - 1][i], distance[n - 1][j]))

    print(ret)
    # fptr.write(str(res) + '\n')
    #
    # fptr.close()
