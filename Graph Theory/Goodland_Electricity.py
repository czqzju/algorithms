#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the pylons function below.
def pylons(k, arr):
    ret = 0
    cur = 0
    while cur < len(arr):
        found = False
        for i in range(k - 1, -1, -1):
            if cur + i >=n: continue
            if arr[cur + i] == 1:
                found = True
                cur = cur + i
                ret += 1
                break
        if found == True:
            cur += k
        else:
            return -1
    return ret

    

if __name__ == '__main__':
    n, k = input().strip().split(" ")
    n, k = (int(n), int(k))
    a = list(map(int, input().split(" ")))
    i, j, trans, flag, loc = 0, 0, 0, 0, 0
    while (i < n):
        trans += 1
        j = i + k - 1
        if (j > n):
            j = n - 1
        while (loc <= j < n and a[j] == 0):
            j -= 1
        if (j < loc):
            print("-1 ")
            flag = 1
            break
        else:
            loc = j + 1
            j += k
            i = j
    if (flag == 0):
        print(trans)
