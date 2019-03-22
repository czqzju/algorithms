#!/bin/python3
#https://www.hackerrank.com/challenges/jeanies-route/problem pypy3
import os
import sys

#
# Complete the jeanisRoute function below.
#
maxDistance = 0
lastNode = -1
def maxDepth(root, visited, except_citites, edges, city):
    global maxDistance
    global  lastNode
    q = []
    q.append([root, 0])
    while len(q):
        cur, curdis = q.pop()
        visited[cur] = True
        if cur in edges:
            for child in edges[cur]:
                if visited[child] or child in except_citites: continue
                if child in city and curdis + edges[cur][child] > maxDistance:
                    lastNode = child
                    maxDistance = curdis + edges[cur][child]
                q.append([child, curdis + edges[cur][child]])




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
    maxLen = 0
    for i in range(1, len(roads) + 2):
        if i not in except_citites and len(edges[i]) > maxLen:
            root = i
            maxLen = len(edges[i])
    maxDepth(root,  visited, except_citites, edges, city)
    global  lastNode
    root = lastNode
    for i in range(0, len(visited)): visited[i] = False
    maxDepth(root, visited, except_citites, edges, city)

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
