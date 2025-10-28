def radixSort(myArray):
    radixArray = [[], [], [], [], [], [], [], [], [], []]
    maxVal = max(myArray)
    exp = 1

    while maxVal // exp > 0:

        while len(myArray) > 0:
            val = myArray.pop()
            radixIndex = (val // exp) % 10
            radixArray[radixIndex].append(val)

        for bucket in radixArray:
            while len(bucket) > 0:
                val = bucket.pop()
                myArray.append(val)
        exp *= 10
    return myArray

def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    leftHalf = arr[:mid]
    rightHalf = arr[mid:]

    def merge(left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result
    
    sortedLeft = mergeSort(leftHalf)
    sortedRight = mergeSort(rightHalf)
    return merge(sortedLeft, sortedRight)


#Python

myArray = [170, 45, 75, 90, 802, 24, 2, 66]
print("Original array:", myArray)
# print("Radix Sort Sorted array:",radixSort(myArray))
print("Merge Sort Sorted array:",mergeSort(myArray))