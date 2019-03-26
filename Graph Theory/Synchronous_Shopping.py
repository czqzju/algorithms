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
    if (vn, vm) in s: s.pop((vn, vm))
    distance[vn][vm] = vv
    s[(vn, vm)] = vv

def shop(n, num, centers, roads):
    global a, distance, edges, s
    INF = sys.maxsize
    distance = [[INF for _ in range(0, 2 ** num)] for _ in range(0, n)]
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
    s = dict()
    push(0, a[0], 0, s)

    while len(s):
        (curNode, types), dis = s.popitem()
        for k, _ in edges[curNode].items():
            push(k, types | a[k], dis + edges[curNode][k], s)
    ret = INF

    for i in range(1, 1 << num):
        for j in range(i, 1 << num):
            if (i | j) == ((1 << num) - 1):
                ret = min(ret, max(distance[n - 1][i], distance[n - 1][j]))
    return ret


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
