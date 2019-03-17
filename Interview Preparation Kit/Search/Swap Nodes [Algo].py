#!/bin/python3

import os
import sys


def find_k(indexes, k):
    h = 1
    if h == k:
        return [k - 1]
    index = [0]
    while h < k:
        h += 1
        res = []
        for i in index:
            if indexes[i][0] != -1:
                res.append(indexes[i][0] - 1)
            if indexes[i][1] != -1:
                res.append(indexes[i][1] - 1)
        if all(x == -1 for x in res):
            return None
        if h == k:
            return res

        index = res


def print_preorder(indexes, index, res):
    if index >= len(indexes):
        return
    if indexes[index][0] != -1:
        print_preorder(indexes, indexes[index][0] - 1, res)
    res.append(index + 1)
    if indexes[index][1] != -1:
        print_preorder(indexes, indexes[index][1] - 1, res)


def swapNodes(indexes, queries):
    ans = []
    for k in queries:
        num = k
        while True:
            res_k = find_k(indexes, num)
            if not res_k:
                break
            else:
                for i in res_k:
                    tmp = indexes[i][0]
                    indexes[i][0] = indexes[i][1]
                    indexes[i][1] = tmp
                num += k
        res = []
        print_preorder(indexes, 0, res)
        ans.append(res)
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = swapNodes(indexes, queries)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()
