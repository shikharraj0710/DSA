arr = [100, -1, 4, 5, 0, 6, 4, 10]

def swap(i, j):
    arr[i], arr[j] = arr[j], arr[i]

for i in range(len(arr) - 1):
    min_index = i
    for j in range(i + 1, len(arr)):
        if arr[min_index] > arr[j]:
            min_index = j
    swap(min_index, i)

print(arr)

# Time Complexity: The time complexity of Selection Sort is O(N2) as there are two nested loops:

# One loop to select an element of Array one by one = O(N)
# Another loop to compare that element with every other Array element = O(N)
# Therefore overall complexity = O(N) * O(N) = O(N*N) = O(N2)