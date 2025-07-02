const arr = [100, -1, 4, 5, 0, 6, 4, 10, -9, -1]

function swap (arr, i, j) {
  ;[arr[i], arr[j]] = [arr[j], arr[i]]
}

function bubbleSort (arr) {
  let length = arr.length
  for (let i = 0; i < length - 1; i++) {
    let swapped = false
    for (let j = 0; j < length - i - 1; j++) {
      if (arr[j] > arr[j + 1]) {
        swap(arr, j, j + 1)
        swapped = true
      }
    }
    if (!swapped) break
  }
  return arr
}

// console.log(bubbleSort(arr))

function selectionSort (arr) {
  for (let i = 0; i < arr.length; i++) {
    let minIndex = i
    for (let j = i + 1; j < arr.length; j++) {
      if (arr[minIndex] > arr[j]) {
        swap(arr, minIndex, j)
      }
    }
  }
  return arr
}

// console.log(selectionSort(arr))

function insertionSort (arr) {
  for (let i = 1; i < arr.length; i++) {
    let currentValue = arr[i]
    let j = i - 1
    while (j >= 0 && currentValue < arr[j]) {
      arr[j + 1] = arr[j]
      j--
    }
    arr[j + 1] = currentValue
  }
  return arr
}

// console.log(insertionSort(arr))

function quickSortPartition (arr, lowIndex, highIndex, pivot) {
  let leftPointer = lowIndex
  let rightPointer = highIndex - 1

  while (leftPointer < rightPointer) {
    while (pivot >= arr[leftPointer] && leftPointer < rightPointer) {
      leftPointer++
    }
    while (pivot <= arr[rightPointer] && leftPointer < rightPointer) {
      rightPointer--
    }
    if (leftPointer < rightPointer) {
      swap(arr, leftPointer, rightPointer)
    }
  }

  if (arr[highIndex] <= arr[leftPointer]) {
    swap(arr, leftPointer, highIndex)
  } else {
    leftPointer = highIndex
  }

  return leftPointer
}

function quickSort (arr, lowIndex, highIndex) {
  if (lowIndex >= highIndex) return

  let pivotIndex =
    Math.floor(Math.random() * (highIndex - lowIndex + 1)) + lowIndex
  let pivot = arr[pivotIndex]

  swap(arr, highIndex, pivotIndex)

  let leftPointer = quickSortPartition(arr, lowIndex, highIndex, pivot)

  quickSort(arr, lowIndex, leftPointer - 1)
  quickSort(arr, leftPointer + 1, highIndex)

  return arr
}

console.log(quickSort(arr, 0, arr.length - 1))
