#!/bin/python3

import math
import os
import random
import re
import sys
import heapq

#
# Complete the 'getCost' function below.
#
# The function accepts WEIGHTED_INTEGER_GRAPH g as parameter.
#

#
# For the weighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] and <name>_to[i]. The weight of the edge is <name>_weight[i].
#
#

def getCost(g_nodes, g_from, g_to, g_weight):
    edges = {}
    end = g_nodes - 1
    start = 0
    for i in range(0, len(g_from)):
        v1 = g_from[i] - 1
        v2 = g_to[i] - 1
        weight = g_weight[i]
        if v1 == v2: continue
        if v1 in edges:
            if v2 in edges[v1]:
                if edges[v1][v2] > weight: edges[v1][v2] = weight
            else: edges[v1][v2] = weight
        else: edges[v1] = {v2: weight}

        if v2 in edges:
            if v1 in edges[v2]:
                if edges[v2][v1] > weight: edges[v2][v1] = weight
            else: edges[v2][v1] = weight
        else:
            edges[v2] = {v1:weight}
    ## use heap
    cost = [[sys.maxsize, i] for i in range(0, g_nodes)]
    visited = set()
    waitingNodes = []
    cost[start][0] = 0
    heapq.heappush(waitingNodes, cost[start])

    while len(waitingNodes):

        curNode= heapq.heappop(waitingNodes)
        curMin = curNode[1]
        if curMin in visited: continue
        if curMin == end: break
        if curMin in edges:
            for k, v in edges[curMin].items():
                if k not in visited:
                    if cost[k] not in waitingNodes:
                        cost[k][0] = v if v > cost[curMin][0] else cost[curMin][0]
                        heapq.heappush(waitingNodes, cost[k])
                    else:
                        newDis =  v if v > cost[curMin][0] else cost[curMin][0]
                        if newDis < cost[k][0]:
                            cost[k] = [newDis, k]
                            heapq.heappush(waitingNodes,cost[k])
        visited.add(curMin)
    print("NO PATH EXISTS" if cost[end][0] == sys.maxsize else cost[end][0])
    # cost = [-1] * g_nodes
    # visited = set()
    # waitingNodes = set()
    # waitingNodes.add(start)
    # cost[start] = 0
    # minLen = sys.maxsize
    # curMin = start
    # while len(waitingNodes):
    #     for node in waitingNodes:
    #         if cost[node] < minLen:
    #             curMin = node
    #             minLen = cost[node]
    #     if curMin == end: break
    #     if curMin in edges:
    #         for k, v in edges[curMin].items():
    #             if k not in visited:
    #                 if k not in waitingNodes:
    #                     cost[k] = v if v > cost[curMin] else cost[curMin]
    #                     waitingNodes.add(k)
    #                 else:
    #                     cost[k] = min(cost[k], v if v > cost[curMin] else cost[curMin])
    #     waitingNodes.remove(curMin)
    #     visited.add(curMin)
    #     minLen = sys.maxsize
    # print("NO PATH EXISTS" if cost[end] == -1 else cost[end])



if __name__ == '__main__':
    g_nodes, g_edges = map(int, input().rstrip().split())

    g_from = [0] * g_edges
    g_to = [0] * g_edges
    g_weight = [0] * g_edges

    for i in range(g_edges):
        g_from[i], g_to[i], g_weight[i] = map(int, input().rstrip().split())

    getCost(g_nodes, g_from, g_to, g_weight)
