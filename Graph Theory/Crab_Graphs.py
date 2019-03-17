#!/bin/python3

import os
import sys

#
# Complete the crabGraphs function below.
#
def crabGraphs(n, t, graph):
    edges = dict()
    countA = [0] * n
    countB = [1] * n
    res = 0
    for i in range(0, len(graph)):
        v1 = graph[i][0] - 1
        v2 = graph[i][1] - 1
        if v1 in edges:
            edges[v1].add(v2)
        else:
            edges[v1] = set()
            edges[v1].add(v2)
        countA[v1] += 1


        if v2 in edges:
            edges[v2].add(v1)
        else:
            edges[v2] = set()
            edges[v2].add(v1)
        countA[v2] += 1

    for i in range(0, n):
        if not countA[i]: continue
        for v in edges[i]:
            if countB[v]:
                countA[i] -= 1
                countB[v] -= 1
                res += 1
                if not countA[i]: break
    return res

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    c = int(input())

    for c_itr in range(c):
        ntm = input().split()

        n = int(ntm[0])

        t = int(ntm[1])

        m = int(ntm[2])

        graph = []

        for _ in range(m):
            graph.append(list(map(int, input().rstrip().split())))

        result = crabGraphs(n, t, graph)
        print(result)

        # fptr.write(str(result) + '\n')

    # fptr.close()
