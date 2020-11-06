#! python3
# very simple selection sort for array

#finding the smallest index
def findSmallest(arr):
    smallest = arr[0]       #storing the smallest value
    smallestIndex = 0       #storing the index of 'smallest'
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallestIndex = i
    return smallestIndex

#iterating through the array
def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

print(selectionSort([4,5,2,6,7,11,9]))
print(selectionSort(['amber', 'jonah', 'adam', 'sarah', 'karen']))
