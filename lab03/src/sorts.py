def insertionSort(arr, size):
    for i in range(1, size):
        key = arr[i]
        
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


def shakerSort(arr, size):
    left = 0
    right = size - 1
    lastSwap = 0

    while left < right:
        for i in range(left, right):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                lastSwap = i

        right = lastSwap

        for i in range(right, left, -1):
            if arr[i - 1] > arr[i]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                lastSwap = i

        left = lastSwap

    return arr


def selectionSort(arr, size):
    for i in range(size - 1):
        minIndex = i

        for j in range(i + 1, size):
            if arr[minIndex] > arr[j]:
                minIndex = j

        arr[minIndex], arr[i] = arr[i], arr[minIndex]

    return arr


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5]
    b = [5, 4, 3, 2, 1]
    c = [4, 2 ,3, 5, 1]

    print(insertionSort(a, 5))
    print(shakerSort(a, 5))
    print(selectionSort(a, 5))

    print(insertionSort(b, 5))
    print(shakerSort(b, 5))
    print(selectionSort(b, 5))

    print(insertionSort(c, 5))
    print(shakerSort(c, 5))
    print(selectionSort(c, 5))

    print(insertionSort([1], 1))
    print(shakerSort([1], 1))
    print(selectionSort([1], 1))

    print(insertionSort([], 0))
    print(shakerSort([], 0))
    print(selectionSort([], 0))

    print(insertionSort(["ab", "make", "draw"], 3))
    print(insertionSort([2, 1, 3, 4, 5], 5))
