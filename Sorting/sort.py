def swap(arr, i, j):
    arr[j], arr[i] = arr[i], arr[j]

def BubbleSort():
    arr = [100, 2, -2, -1, 0, 4, 2, 40]
    n = len(arr)

    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                swap(arr, j, j + 1)
                swapped = True
        
        if swapped == False:
            break

    print(arr)

def SelectionSort():
    arr = [100, 2, -2, -1, 0, 4, 2, 40]
    n = len(arr)

    for i in range(n - 1):
        minimum = i
        for j in range(i + 1, n):
            if arr[minimum] > arr[j]:
                minimum = j
        
        swap(arr, minimum, i)
    
    print(arr)

def InsertionSort():
    arr = [100, 2, -2, -1, 0, 4, 2, 40]
    n = len(arr)

    for i in range(1, n):
        currentValue = arr[i]
        j = i - 1

        while(j >= 0 and arr[j] > currentValue):
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = currentValue

    print(arr)

class QuickSort:
    def __init__(self, arr):
        self.arr = arr
        

    def quickSort(self, arr, lowIndex, highIndex):
        if lowIndex >= highIndex:
            return
        pivot = arr[highIndex]
        leftPointer = lowIndex
        rightPointer = highIndex

        while(leftPointer < rightPointer):
            while(arr[leftPointer] <= pivot and leftPointer < rightPointer):
                leftPointer += 1
            while(arr[rightPointer] >= pivot and leftPointer < rightPointer):
                rightPointer -= 1
            swap(arr, leftPointer, rightPointer)

        swap(arr, leftPointer, highIndex)

        self.quickSort(arr, lowIndex, leftPointer - 1)
        self.quickSort(arr, leftPointer + 1, highIndex)

    def print(self):
        print(self.arr)


class MergeSort:
    def mergeSort(self, arr):
        if len(arr) <= 1:
            return
        length = len(arr)
        midPoint = length // 2

        rightHalf = arr[:midPoint]
        leftHalf = arr[midPoint:]

        self.mergeSort(rightHalf)
        self.mergeSort(leftHalf)

        self.merge(arr, leftHalf, rightHalf)

    
    def merge(self, result, leftArray, rightArray):
        i = 0
        j = 0
        k = 0

        while(i < len(leftArray) and j < len(rightArray)):
            if leftArray[i] <= rightArray[j]:
                result[k] = leftArray[i]
                i += 1
            else:
                result[k] = rightArray[j]
                j += 1
            k += 1

        while(i < len(leftArray)):
            result[k] = leftArray[i]
            k += 1
            i += 1
        
        while(j < len(rightArray)):
            result[k] = rightArray[j]
            k += 1
            j += 1


BubbleSort()
SelectionSort()
InsertionSort()
quickSortObj = QuickSort([100, 2, -2, -1, 0, 4, 2, 40])
quickSortObj.quickSort(quickSortObj.arr, 0, len(quickSortObj.arr) - 1)
quickSortObj.print()

mergeSortObj = MergeSort()
arr = [100, 2, -2, -1, 0, 4, 2, 40]
mergeSortObj.mergeSort(arr)
print(arr)


def mergeSort(arr):
    length = len(arr)
    if length < 2:
        return 
    
    midPoint = length // 2

    leftArray = arr[:midPoint]
    rightArray = arr[midPoint:]

    mergeSort(leftArray)
    mergeSort(rightArray)

    merge(arr, leftArray, rightArray)


def merge(arr, leftHalf, rightHalf):
    i = 0
    j = 0
    k = 0

    while(i < len(leftHalf) and j < len(rightHalf)):
        if leftHalf[i] <= rightHalf[j]:
            arr[k] = leftHalf[i]
            i += 1
        else: 
            arr[k] = rightHalf[j]
            j += 1
        k += 1
    
    while(i < len(leftHalf)):
        arr[k] = leftHalf[i]
        i += 1
        k += 1
    
    while(j < len(rightHalf)):
        arr[k] = rightHalf[j]
        j += 1
        k += 1

arr2 = [100, 2, -2, -1, 0, 4, 2, 40]
mergeSort(arr2)
print(arr2)


