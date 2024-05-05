arr = [100, -1, 4, 5, 0, 6, 4, 10]

def swap(i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

for i in range(len(arr) - 1):
    for j in range(i + 1, len(arr)):
        if arr[i] > arr[j]:
            swap(i, j)

print(arr)



