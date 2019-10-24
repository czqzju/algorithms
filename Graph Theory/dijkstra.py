#!/bin/python3

from math import radians, cos, sin,sqrt, atan2
import sys

def computeDis(lat_1, lng_1, lat_2, lng_2):
  lat_1, lng_1, lat_2, lng_2 = map(radians, [lat_1, lng_1, lat_2, lng_2])
  R = 6371
  diff_lat = lat_2 - lat_1
  diff_lng = lng_2 - lng_1
  a = (sin(diff_lat/2))**2 + cos(lat_1) * cos(lat_2) * (sin(diff_lng/2))**2
  c = 2 * atan2(sqrt(a), sqrt(1-a))
  return R * c

def getAdjMatrix(lats, lngs, maxDis):
  edges = dict()
  for i in range(len(lats) - 1):
    for j in range(i + 1, len(lats)):
      dis = computeDis(lats[i], lngs[i], lats[j], lngs[j])
      if(dis > maxDis): continue
      if i in edges: edges[i][j] = dis
      else: edges.setdefault(i, dict({j:dis}))
      if j in edges: edges[j][i] = dis
      else: edges.setdefault(j, { i : dis })
  return edges


if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        num = int(input())
        lats = []
        lngs = []
        cities = []
        for _ in range(num):
            lat_lng_cities = input().split()
            lats.append(float(lat_lng_cities[0]))
            lngs.append(float(lat_lng_cities[1]))
            if len(lat_lng_cities) > 3:

                cities.append(" ".join(lat_lng_cities[i] for i in range(2, len(lat_lng_cities))))
            else:
                cities.append(lat_lng_cities[2])
        maxDis = float(input())
        adj_matrix = getAdjMatrix(lats, lngs, maxDis)
        u = dict()
        s = dict()
        s.setdefault(0, 0)
        parent = []
        for i in range(num): parent.append(-1)
        for i in range(1, num):
            if(0 in adj_matrix and i in adj_matrix[0]):
                u.setdefault(i, adj_matrix[0][i])
                parent[i] = 0
            else:
                u.setdefault(i, sys.float_info.max)
        noRoute = False
        while(len(u)):
            curNearCity = min(u, key=u.get)
            curNearDis = u.pop(curNearCity)
            if(curNearDis == sys.float_info.max):
                noRoute = True
                break
            if(curNearCity == num - 1):
                res = []
                curCity = curNearCity
                while(curCity != -1):
                    res.append(curCity)
                    curCity = parent[curCity]
                print(", ".join(cities[res[i]] for i in range(len(res) - 1, -1, -1)))
                break
            s.setdefault(curNearCity, curNearDis)
            if curNearCity in adj_matrix:
                for k in adj_matrix[curNearCity]:
                    if k in s: continue
                    if curNearDis + adj_matrix[curNearCity][k] < u[k]:
                        u[k] = curNearDis + adj_matrix[curNearCity][k]
                        parent[k] = curNearCity
        if noRoute:
            print("Not possible")
            continue