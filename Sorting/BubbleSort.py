arr = [100, -1, 4, 5, 0, 6, 4, 10]
n = len(arr)

def swap(i, j):
    arr[i], arr[j] = arr[j], arr[i]

for i in range(n):
    swapped = False
    for j in range(0, n - i -1):
        if arr[j] > arr[j + 1]:
            swap(j, j + 1)
            swapped = True
        
    if swapped == False:
        break

print(arr)

# In Bubble Sort algorithm, 

# traverse from left and compare adjacent elements and the higher one is placed at right side. 
# In this way, the largest element is moved to the rightmost end at first. 
# This process is then continued to find the second largest and place it and so on until the data is sorted.

# Time Complexity: O(N2)
