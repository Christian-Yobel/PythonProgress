#! python3
# recursion exercises

#sum of a list of number
def sumOf(list):
    if len(list) == 1:
        return list[0]
    else:
        return list.pop() + sumOf(list)

    
#alternative with lambda
sums = lambda x: x[0] if len(x) == 1 else x[0]+sums(x[1:])
##def sums(x):
##    if len(x) == 1:
##        return x[0]
##    else:
##        return x[0] + sums(x[1:])

print(sumOf([1,3,6]))               #returns 10
print(sums([5,1,2]))                #returns 8


#sums of list with nested list
def theSums(list):
    total = 0
    for i in list:
        if type(i) is type([]):
            total = total + theSums(i)
        else:
            total = total + theSums(list[1:])
    return total
print(theSums([1, 2, [3,4], [5,6]]))
            

#converting int to a word of base 26
def convert(int):
    base = 26
    strings = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if int < base:
        return strings[int]
    else:
        return convert(int//base) + strings[int%base]

print(convert(28))                  #returns BC
print(convert(51246))               #returns CXVA


#factorial of a non-negative integer
def factorial(int):
    if int <= 1:
        return int
    else:
        return int*factorial(int-1)

print(factorial(5))                 #returns 120


#calculate the power of with a recursion
def powerOf(int, pw):
    if pw == 0:
        return 1
    elif pw == 1:
        return int
    else:
        return int * powerOf(int, pw-1)
#lambda version
power = lambda x,y: 1 if y==0 else(x if y==1 else x*power(x,y-1))

print(powerOf(4,5))                 #returns 1024
print(power(4,5))                   #returns 1024


#finding the greatest common divisor of two integers
def cmDiv(a,b):
    high = max(a,b)
    low = min(a,b)

    if low == 0:
        return high
    elif low == 1:
        return 1
    else:
        return cmDiv(low, high%low)

print(cmDiv(123,7))                 #returns 1
print(cmDiv(144,24))                #returns 24
