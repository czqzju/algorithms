#!/bin/python3
#https://www.hackerrank.com/challenges/jeanies-route/problem
import os
import sys

#
# Complete the jeanisRoute function below.
#
maxDistance = 0
def maxDepth(root, visited, except_citites, edges):
    global maxDistance
    visited[root] = True
    childrenDeps = []
    if root in edges:
        for child in edges[root]:
            if visited[child] or child in except_citites: continue
            childrenDeps.append(maxDepth(child, visited, except_citites, edges) + edges[root][child])
        list.sort(childrenDeps, reverse= True)
        if len(childrenDeps) >= 2:
            curDis = childrenDeps[0] + childrenDeps[1]
            if curDis > maxDistance: maxDistance = curDis
            return childrenDeps[0]
        elif len(childrenDeps) == 1:
            curDis = childrenDeps[0]
            if curDis > maxDistance: maxDistance = curDis
            return childrenDeps[0]
        else:
            return 0


def jeanisRoute(city, roads):
    edges = dict()
    for i in range(0, len(roads)):
        v1 = roads[i][0]
        v2 = roads[i][1]
        dis = roads[i][2]

        if v1 in edges:
            edges[v1][v2] = dis
        else:
            edges[v1] = dict()
            edges[v1][v2] = dis

        if v2 in edges:
            edges[v2][v1] = dis
        else:
            edges[v2] = dict()
            edges[v2][v1] = dis
    non_letters = []
    except_citites = set()
    for k, v in edges.items():
        if k not in city and len(v) == 1: non_letters.append(k)
    while len(non_letters):
        cur = non_letters.pop()
        for k, v in edges[cur].items():
            del edges[k][cur]
            if k not in city and len(edges[k]) == 1: non_letters.append(k)
        except_citites.add(cur)

    totalRoad = sum(roads[i][2] for i in range(0, len(roads)) if roads[i][0] not in except_citites and roads[i][1] not in except_citites) * 2
    visited = [False] * (len(roads) + 2)
    root = 1
    rootLen = 0
    for i in range(1, len(roads) + 2):
        if i not in except_citites and len(edges[i]) > rootLen:
            root = i
            rootLen = len(edges[i])
    maxDepth(root, visited, except_citites, edges)
    return totalRoad - maxDistance

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    city = set(list(map(int, input().rstrip().split())))

    roads = []

    for _ in range(n-1):
        roads.append(list(map(int, input().rstrip().split())))

    result = jeanisRoute(city, roads)
    print(result)

    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
