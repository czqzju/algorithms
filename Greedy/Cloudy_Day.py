#!/bin/python3
#https://www.hackerrank.com/challenges/cloudy-day/problem
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
    cloudsOfCity = [0] * len(locOfCities)
    for i in range(len(y)):
        left = max(1, y[i] - r[i])
        right = y[i] + r[i]
        l_city = bisect.bisect_left(locOfCities, left)
        r_city = bisect.bisect_right(locOfCities, right)
        if l_city == len(locOfCities): continue
        cloudsOfCity[l_city] += 1
        if r_city < len(locOfCities):
            if locOfCities[r_city] > y[i] + r[i]:
                cloudsOfCity[r_city] -= 1
            else:
                if r_city + 1 < len(locOfCities):
                    cloudsOfCity[r_city + 1] -= 1

    sumOfSunnyCities = 0
    preSum = []
    citiesWithOne = []
    for i in range(len(cloudsOfCity)):
        if i != 0:
            cloudsOfCity[i] += cloudsOfCity[i - 1]
        if cloudsOfCity[i] == 0:
            sumOfSunnyCities += cities[locOfCities[i]]
        elif cloudsOfCity[i] == 1:
            citiesWithOne.append(locOfCities[i])
            prePopu = 0
            if len(preSum) > 0:
                prePopu += preSum[len(preSum) - 1]
            preSum.append(prePopu + cities[locOfCities[i]])
    curMaxPopu = 0
    for i in range(len(y)):
        left = max(1, y[i] - r[i])
        right = y[i] + r[i]
        l_city = bisect.bisect_left(citiesWithOne, left)
        r_city = bisect.bisect_right(citiesWithOne, right)
        if l_city >= len(citiesWithOne) or r_city == 0: continue
        if r_city == len(citiesWithOne) or citiesWithOne[r_city] > y[i] + r[i]: r_city -= 1

        if l_city > 0:
            curMaxPopu = max(curMaxPopu, preSum[r_city] - preSum[l_city - 1])
        else:
            curMaxPopu = max(curMaxPopu, preSum[r_city])
    return curMaxPopu + sumOfSunnyCities

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fr = open('data.txt', 'rt')

    n = int(fr.readline())


    p = list(map(int, fr.readline().rstrip().split()))

    x = list(map(int, fr.readline().rstrip().split()))


    m = int(fr.readline())

    y = list(map(int, fr.readline().rstrip().split()))

    r = list(map(int, fr.readline().rstrip().split()))

    result = maximumPeople(p, x, y, r)
    print(result)

    fr.close()

    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
