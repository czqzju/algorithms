#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    totalPrice = sum(bill[i] for i in range(0, len(bill)) if not(i == k))
    if totalPrice//2 == b:
        print("Bon Appetit")
    else:
        print(b-totalPrice//2)

if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)

    l = ['a','b','c']
    l.reverse()