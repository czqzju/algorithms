import heapq
import time
import sys

#
# n = 50000
# s = set()
# time1 = time.time()
# for i in range(0, n): s.add(i)
# while len(s):
#     curMin = sys.maxsize
#     for item in s:
#         if item < curMin: curMin = item
#     s.remove(curMin)
# time2 = time.time()
# print("%d个数字的set查询删除时间%s"%(n, time2 - time1))
#
# heap = []
# for i in range(0, n): s.add(i)
#
# time1 = time.time()
# for item in s: heapq.heappush(heap, item)
# while len(heap):
#     heapq.heappop(heap)
# time2 = time.time()
# print("%d个数字的heap查询删除时间%s"%(n, time2 - time1))
a = [1,2,3,4]
a.reverse()
print(a)





