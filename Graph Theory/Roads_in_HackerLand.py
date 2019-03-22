#!/bin/python3

import os
import sys

#
# Complete the roadsInHackerland function below.

def findParent(node, parent):
    while not node == parent[node]: node = parent[node]
    return parent[node]

def roadsInHackerland(n, roads):
    roads.sort(key = lambda road:road[2])
    parent = [i for i in range(0, n)]
    numOfNodes = [1] * n
    edges = {}
    cntOfEdges = 0

    for i in range(0, n):
        v1 = roads[i][0] - 1
        v2 = roads[i][1] - 1
        value = roads[i][2]
        if v1 in edges and v2 in edges:
            p1 = findParent(v1, parent)
            p2 = findParent(v2, parent)
            if p1 == p2: continue
            else:
                edges[v1][v2] = value
                edges[v2][v1] = value
                parent[v2] = p1
                cntOfEdges += 1

        elif v1 in edges and v2 not in edges:
            p1 = findParent(v1, parent)
            edges[v1][v2] = value
            edges[v2] = {v1: value}
            parent[v2] = p1
            cntOfEdges += 1
        elif v1 not in edges and v2 in edges:
            p2 = findParent(v2, parent)
            edges[v2][v1] = value
            edges[v1] = {v2: value}
            parent[v1] = p2
            cntOfEdges += 1
        else:
            edges[v1] = {v2 : value}
            edges[v2] = {v1 : value}
            parent[v2] = v1
            cntOfEdges += 1
        if cntOfEdges == n - 1: break

    q = [i for i in range(0, n) if len(edges[i]) == 1]

    dis = 0
    while len(q):
        cur = q.pop()
        if len(edges[cur]) == 0: break
        for k, v in edges[cur].items():
            dis += numOfNodes[cur] * (n - numOfNodes[cur]) * 2 ** v

            del edges[k][cur]
            numOfNodes[k] += 1
            if len(edges[k]) == 1: q.append(k)
        del edges[cur]

    return dis

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    roads = []

    for _ in range(m):
        roads.append(list(map(int, input().rstrip().split())))

    result = roadsInHackerland(n, roads)
    print(result)

    # fptr.write(result + '\n')
    #
    # fptr.close()
