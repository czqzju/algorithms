#!/bin/python3

import math
import os
import random
import re
import sys
from bisect import *

# Complete the triplets function below.
def triplets(a, b, c):
   a = sorted(set(a))
   b = sorted(set(b), reverse=True)
   c = sorted(set(c))
   return sum(bisect(a, x) * bisect(c, x) for x in b)



if __name__ == '__main__':

    lenaLenbLenc = input().split()

    lena = int(lenaLenbLenc[0])

    lenb = int(lenaLenbLenc[1])

    lenc = int(lenaLenbLenc[2])

    arra = list(map(int, input().rstrip().split()))

    arrb = list(map(int, input().rstrip().split()))

    arrc = list(map(int, input().rstrip().split()))

    ans = triplets(arra, arrb, arrc)

    print(ans)
