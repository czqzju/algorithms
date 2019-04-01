#!/bin/python3

import math
import os
import random
import re
import sys
import bisect

# Complete the maximumPeople function below.
def maximumPeople(p, x, y, r):
    cities = {}
    for i in range(len(x)):
        if x[i] in cities: cities[x[i]] += p[i]
        else: cities[x[i]] = p[i]
    locOfCities = list(cities.keys())
    locOfCities.sort()
    citiesOfCloud = {}
    cloudsOfCity = {}
    for i in range(len(y)):
        left = max(1, y[i] - r[i])
        l_city = bisect.bisect_left(locOfCities, left)
        while l_city < len(locOfCities) and locOfCities[l_city] in range(y[i] - r[i], y[i] + r[i] + 1):
            if y[i] in citiesOfCloud: citiesOfCloud[y[i]].add(locOfCities[l_city])
            else:
                citiesOfCloud[y[i]] = set(locOfCities[l_city])
            if locOfCities[l_city] in cloudsOfCity: cloudsOfCity[locOfCities[l_city]] += 1
            else: cloudsOfCity[locOfCities[l_city]] = 1
            l_city += 1
    sumOfSunnyCities = sum(cities[city] for city in cloudsOfCity if cloudsOfCity[city] == 0)
    curMaxPopuOfCloud = 0
    for i in range(len(y)):
        if len(citiesOfCloud):
            sumOfOneCloud = sum(cities[k] for k in citiesOfCloud if cloudsOfCity[k] == 1)
            curMaxPopuOfCloud = max(sumOfOneCloud, curMaxPopuOfCloud)
    return sumOfSunnyCities + curMaxPopuOfCloud

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = list(map(int, input().rstrip().split()))

    x = list(map(int, input().rstrip().split()))

    m = int(input())

    y = list(map(int, input().rstrip().split()))

    r = list(map(int, input().rstrip().split()))

    result = maximumPeople(p, x, y, r)

    print(result)

    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
