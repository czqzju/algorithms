#coding=UTF-8
import random

class InsertSort():

    def InsertSort(self, randomlist):
        newList = [0] * 10
        newList[0] = randomlist[0]
        for i in range(1,len(randomlist)):
            key = randomlist[i]
            j = i
            while( j > 0 ):
                if(newList[j-1] > key):
                    newList[j] = newList[j-1]
                    j = j - 1
                else:
                    break
            newList[j] = key


class MergeSort():

    def MergeSort(self, randomlist, p, r):
        q = int((r+p)/2)
        if(q > p):
            # print(p, q, r)
            self.MergeSort(randomlist, p, q)
            self.MergeSort(randomlist, q+1, r)
            self.MergeSubArray(randomlist, p, q, r)
        self.MergeSubArray(randomlist, p, q, r)
        # print(self.randomlist[p:r+1])

    def MergeSubArray(self, randomlist, p, q, r):
        n1 = q - p + 1
        n2 = r - q
        A = [0 for i in range(n1)]
        B = [0 for i in range(n2)]
        index1 = index2 = 0
        for i in range(p, q+1):
            A[index1] = randomlist[i]
            index1 = index1 + 1
        for i in range(q+1, r+1):
            B[index2] = randomlist[i]
            index2 = index2 + 1

        i = j = 0
        index = p
        while(i < n1 and j < n2):
            if(A[i] < B[j]):
                randomlist[index] = A[i]
                index = index + 1
                i = i + 1
            else:
                randomlist[index] = B[j]
                index = index + 1
                j = j + 1
        if(i < n1):
            for resIndex in range(i, n1):
                randomlist[index] = A[resIndex]
                index = index + 1
        elif(j < n2):
            for resIndex in range(j, n2):
                randomlist[index] = B[resIndex]
                index = index + 1



class MaxHeapSort():

    def MaxHeapSort(self, randomlist):
        if(len(randomlist)-1 < 1):
            print("Heap underflow")
            return
        self.buildMaxHeap(randomlist, len(randomlist)-1)
        # print(randomlist)
        heap_size = len(randomlist) - 1
        while(heap_size > 1):
            maxVal = randomlist[1]
            randomlist[1] = randomlist[heap_size]
            randomlist[heap_size] = maxVal
            self.adjustMaxHeap(randomlist, heap_size - 1, 1)
            heap_size = heap_size - 1

    def buildMaxHeap(self, randomlist, heap_size):
        if (len(randomlist) - 1 < 1):
            print("Heap underflow")
            return
        i = int(heap_size / 2)
        while(i > 0):
            self.adjustMaxHeap(randomlist, heap_size, i)
            i = i - 1

    def adjustMaxHeap(self, randomlist, heap_size, index):
        l = 2 * index
        r = 2 * index + 1
        if(l <= heap_size and randomlist[l] > randomlist[index]):
                maxV = randomlist[l]
                largest = l
        else:
            maxV = randomlist[index]
            largest = index

        if(r <= heap_size and randomlist[r] > maxV):
            maxV = randomlist[r]
            largest = r

        if(largest == index):
            return
        else:
            tmpV = randomlist[index]
            randomlist[index] = maxV
            randomlist[largest] = tmpV
            self.adjustMaxHeap(randomlist, heap_size, largest)

class QuitSort():
    def QuitSort(self, randomlist, p, r):
        if(p < r):
            q = self.Partition(randomlist, p, r)
            self.QuitSort(randomlist, p, q - 1)
            self.QuitSort(randomlist, q + 1, r)

    def Partition(self, randomlist, p, r):
        x = randomlist[r]
        i = p - 1
        for j in range(p, r):
            if(randomlist[j] <= x):
                i = i + 1
                if(i != j):
                    self.Exchange(randomlist, i, j)
        self.Exchange(randomlist, i + 1, r)
        return i + 1


    def Exchange(self, randomlist, i, j):
        tmpV = randomlist[i]
        randomlist[i] = randomlist[j]
        randomlist[j] = tmpV

class CountSort():
    def CountSort(self, randomlist, B, k):
        C = []
        for i in range(0, k+1):
            C.append(0)
        for i in range(1, len(randomlist)):
            C[randomlist[i]] = C[randomlist[i]] + 1
        for i in range(1, k+1):
            C[i] = C[i] + C[i-1]

        j = len(randomlist) - 1
        while(j >= 1):
            B[C[randomlist[j]]] = randomlist[j]
            C[randomlist[j]] = C[randomlist[j]] - 1
            j = j - 1





if __name__ == '__main__':
    list = []
    num = 100
    for i in range(1, num+1):
        list.append(i)
    randomlist = random.sample(list, num)

    #Insert sort
    # test = InsertSort()
    # test.InsertSort(randomlist)

    #Merge sort
    # merge = MergeSort()
    # merge.MergeSort(randomlist, 0, len(randomlist)-1)

    #Heap sort
    # randomlist.append(0)
    # tmpV = randomlist[len(randomlist) - 1]
    # randomlist[len(randomlist) - 1] = randomlist[0]
    # randomlist[0] = tmpV
    # heap = MaxHeapSort()
    # print(randomlist)
    # heap.MaxHeapSort(randomlist)
    # print(randomlist)

    #Quit sort
    # randomlist.append(0)
    # tmpV = randomlist[len(randomlist) - 1]
    # randomlist[len(randomlist) - 1] = randomlist[0]
    # randomlist[0] = tmpV
    # quitSort = QuitSort()
    # print(randomlist)
    # quitSort.QuitSort(randomlist, 1, len(randomlist) - 1)
    # print(randomlist)

    #CountSort
    randomlist.append(0)
    tmpV = randomlist[len(randomlist) - 1]
    randomlist[len(randomlist) - 1] = randomlist[0]
    randomlist[0] = tmpV
    countSort = CountSort()
    print(randomlist)
    B = []
    for i in range(0, len(randomlist)):
        B.append(0)
    countSort.CountSort(randomlist, B, 100)
    print(B)


