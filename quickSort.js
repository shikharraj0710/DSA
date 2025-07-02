const arr = [100, -1, 4, 5, 0, 6, 4, 10, -9, -1]

function swap (arr, i, j) {
  ;[arr[i], arr[j]] = [arr[j], arr[i]]
}

const quickSortPartition = (arr, lowIndex, highIndex, pivot) => {
  let leftPointer = lowIndex
  let rightPointer = highIndex - 1

  while (leftPointer < rightPointer) {
    while (arr[leftPointer] <= pivot && leftPointer < rightPointer) {
      leftPointer++
    }
    while (arr[rightPointer] >= pivot && leftPointer < rightPointer) {
      rightPointer--
    }
    if (leftPointer < rightPointer) {
      swap(arr, leftPointer, rightPointer)
    }
  }
  if (arr[leftPointer] >= arr[highIndex]) {
    swap(arr, leftPointer, highIndex)
  } else {
    leftPointer = highIndex
  }

  return leftPointer
}

function quickSort (arr, lowIndex, highIndex) {
  if (lowIndex >= highIndex) return

  const pivotIndex =
    Math.floor(Math.random() * (highIndex - lowIndex + 1)) + lowIndex

  const pivot = arr[pivotIndex]

  swap(arr, pivotIndex, highIndex)

  const leftPointer = quickSortPartition(arr, lowIndex, highIndex, pivot)

  quickSort(arr, lowIndex, leftPointer - 1)
  quickSort(arr, leftPointer + 1, highIndex)

  return arr
}

console.log(quickSort(arr, 0, arr.length - 1))
