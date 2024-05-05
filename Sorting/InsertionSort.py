arr = [100, -1, 4, 5, 0, 6, 4, 10]

for i in range(1, len(arr)):
    current = arr[i]
    j = i - 1
    while(j >= 0 and arr[j] > current):
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = current

print(arr)

# Time Complexity of Insertion Sort :::
# Best case: O(n), If the list is already sorted, where n is the number of elements in the list.
# Average case: O(n2), If the list is randomly ordered
# Worst case: O(n2), If the list is in reverse order