#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the abbreviation function below.
def check(a, b):
    if len(b) > len(a):
        return False
    elif len(b) == len(a):
        if len(b) == 0 or b == a.upper():
            return True
        else:
            return False
    else:
        if len(b) == 0:
            if a.lower() == a:
                return True
            else:
                return False
        else:
            if a[-1].isupper():
                if a[-1] == b[-1]:
                    return check(a[:-1], b[:-1])
                else:
                    return False
            else:
                return check(a[:-1] + a[-1].upper(), b) or check(a[:-1], b)


def abbreviation(a, b):
    flag = check(a, b)
    if flag:
        return "YES"
    else:
        return "NO"


if __name__ == '__main__':


    q = int(input())

    for q_itr in range(q):
        a = input()

        b = input()

        result = abbreviation(a, b)

        print(result)

