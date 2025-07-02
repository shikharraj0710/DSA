def twoSum(arr, target):
    complementDict = {}
    for i in range(len(arr)):
        complement = target - arr[i]
        if complement in complementDict:
            return [complementDict[complement], i]
        complementDict[arr[i]] = i 
        
print(twoSum([2, 5, 6, -1, 0, 7], 1))