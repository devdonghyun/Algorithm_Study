# Selection Sort

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
for i in range(len(array)-1):
    min = array[i]
    index = i
    for j in range(i+1, len(array)):
        if min > array[j]:
            min = array[j]
            index = j
    array[i], array[index] = array[index], array[i]

print(array)


# Insertion Sort
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i):
        if array[i] < array[j]:
            val = array.pop(i)
            array.insert(j, val)
            break

print(array)

# BOOK - Insertion Sort
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
        else:
            break

print(array)

# Quick Sort

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]


def quickSort(array, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        while left <= end and array[left] <= array[pivot]:
            left += 1
        while right > start and array[right] >= array[pivot]:
            right -= 1

        if left > right:
            array[pivot], array[right] = array[right], array[pivot]
        else:
            array[left], array[right] = array[right], array[left]

    quickSort(array, start, right-1)
    quickSort(array, right+1, end)


quickSort(array, 0, len(array)-1)
print(array)


# Count Sort

array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

count = [0] * (max(array) + 1)

for i in range(len(array)):
    count[array[i]] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=' ')
