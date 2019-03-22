#!/bin/python3
#https://www.hackerrank.com/challenges/rust-murderer/problem
import os
import sys

#
# Complete the rustMurdered function below.
#
def rustMurderer(n, roads, s):
    distance = [1] * n
    edges = dict()

    for i in range(0, len(roads)):
        v1 = roads[i][0] - 1
        v2 = roads[i][1] - 1
        if v1 in edges: edges[v1].add(v2)
        else: edges[v1] = set([v2])
        if v2 in edges: edges[v2].add(v1)
        else: edges[v2] = set([v1])

    not_visited = edges[s] if s in edges else set()
    newly_visited = set()
    curr_dist = 2
    while len(not_visited) > 0:
        for i in not_visited:
            diff = not_visited | edges[i]
            if len(diff) < n:
                distance[i] = curr_dist
                newly_visited.add(i)
        not_visited = not_visited - newly_visited
        newly_visited = set()
        curr_dist += 1
    del distance[s]
    return distance

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
