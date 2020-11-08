#! python3
#binary search in recursive function

def searchs(list, target):
    low = 0
    high = len(list) - 1
    mid = int((high+low)/2)
    if target == list[mid]:
        print(str(target) + ' found at index: ' + str(mid))
        return list[mid]
    if list[mid] > target:
        return searchs(list[:mid],target)
    else:
        return searchs(list[mid:],target)


a = ['adam', 'bryan','faraday','gabe','monty', 'susan','zazie']
b = [1,5,6,7,9,12,23,63,123,323,745,885,3473]

searchs(a, 'gabe')
searchs(b, 23)
