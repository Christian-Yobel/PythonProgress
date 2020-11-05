#! python3
# trying out binary search


def binary_search(list, target):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = int((high+low)/2)
        if list[mid] == target:
            print('the target is at index ' + str(mid))
            return mid
        elif list[mid] < target:
            low = mid+1
            print('guesses: ' + str(list[mid]) + ', too low')
        else:
            high = mid-1
            print('guesses: ' + str(list[mid]) + ', too high')

numbers = []
for i in range(101):
    numbers.append(i)

name = ['andre', 'aditya', 'bram', 'chris', 'emily', 'gloria', 'susan']
    
binary_search(numbers, 61)
binary_search(name, 'susan')
