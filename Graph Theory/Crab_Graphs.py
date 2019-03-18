#!/bin/python3
#https://www.hackerrank.com/challenges/crab-graphs/problem

import sys

#
# Complete the crabGraphs function below.
#
def max_flow(s, t, cap):
    parent = [-1] * (t + 1)
    maxflow = 0
    cnt = 0

    while BFS(s, t, cap, parent):
        pathFlow = sys.maxsize
        v = t
        while not v is s:
            u = parent[v]
            pathFlow = cap[u][v] if cap[u][v] < pathFlow else pathFlow
            v = u

        v = t
        while not v is s:
            u = parent[v]
            cap[u][v] -= pathFlow
            cap[v][u] += pathFlow
            v = u
        maxflow += pathFlow
        cnt += 1
    print(cnt)
    return maxflow

def BFS(s, t, cap, parent) :
    visited = [False] * (t + 1)
    q = list()
    q.append(s)
    visited[s] = True
    parent[s] = -1
    while len(q) > 0:
        cur = q.pop()
        for i in range(0, t + 1):
            if not visited[i] and cap[cur][i] > 0 :
                q.append(i)
                visited[i] = True
                parent[i] = cur
    return visited[t] is True


def crabGraphs(n, t, graph):

    cap = [[0] * (n*2+2) for _ in range(0, n *2 + 2)]
    s = n * 2
    des = s + 1

    for i in range(0, len(graph)):
        v1 = graph[i][0] - 1
        v2 = graph[i][1] - 1

        cap[2 * v1][2 * v2 + 1] = 1
        cap[2 * v2][2 * v1 + 1] = 1
        cap[s][2 * v1] += 1
        cap[s][2 * v2] += 1
    for i in range(0, n):
        cap[2 * i + 1][des] = 1
        cap[s][2 * i] = t if cap[s][2 * i] > t else cap[s][2 * i]

    # print(sum(cap[i][101] for i in range(0, 102)))
    return max_flow(s, des, cap)

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
