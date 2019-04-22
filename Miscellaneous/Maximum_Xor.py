# https://www.hackerrank.com/challenges/maximum-xor/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=miscellaneous
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxXor function below.

class Trie:

    def __init__(self):
        self.head = {}

    def add_trie(self, data):
        curNode = self.head
        bins = "{:032b}".format(data)
        for k in bins:
            num = int(k)
            if  not num in curNode:
                curNode.setdefault(num, {})
            curNode = curNode[num]
        curNode['*'] = None

    def find_max_xor(self, data):
        curNode = self.head
        bins = "{:032b}".format(data)

        b = ''
        for k in bins:
            num = int(k)
            op = num ^ 1
            if op in curNode:
                num = op
            b += str(num)
            curNode = curNode[num]
        return data ^ int(b, 2)



def maxXor(arr, queries):
    trie = Trie()
    for i in range(len(arr)):
        trie.add_trie(arr[i])
    res = []
    for i in range(len(queries)):
        curMax = 0
        curMax = max(curMax, trie.find_max_xor(queries[i]))
        res.append(curMax)
    return res



if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    m = int(input())

    queries = []

    for _ in range(m):
        queries_item = int(input())
        queries.append(queries_item)

    result = maxXor(arr, queries)

    print(result)

    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')
    #
    # fptr.close()
