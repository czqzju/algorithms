#!/bin/python3
#https://www.hackerrank.com/challenges/rust-murderer/problem
import os
import sys

#
# Complete the rustMurdered function below.
#
def rustMurderer(n, roads, s):
    allNodes = set()
    distance = [0] * n
    visited = [False] * n
    edges = dict()
    for i in range(0, n):
        allNodes.add(i)
        edges[i] = set([i])
    for i in range(0, len(roads)):
        v1 = roads[i][0] - 1
        v2 = roads[i][1] - 1
        if v1 in edges: edges[v1].add(v2)
        if v2 in edges: edges[v2].add(v1)

    for k in edges:
        edges[k] = allNodes.difference(edges[k])

    q = [s]
    visited[s] = True
    while len(q):
        cur = q.pop()
        if cur in edges:
            for child in edges[cur]:
                if not visited[child]:
                    distance[child] = distance[cur] + 1
                    visited[child] = True
                    q.append(child)
    return [distance[i] for i in range(0, n) if not i == s]


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        roads = []

        for _ in range(m):
            roads.append(list(map(int, input().rstrip().split())))

        s = int(input())

        result = rustMurderer(n, roads, s - 1)
        print(result)

    #     fptr.write(' '.join(map(str, result)))
    #     fptr.write('\n')
    #
    # fptr.close()
