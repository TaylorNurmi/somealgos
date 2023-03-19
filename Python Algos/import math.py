import math

def reverse(array):
    for i in range(math.floor((len(array)/2))):
        array[i], array[len(array) - i-1] = array[len(array) - i-1], array[i]
    return array
print(reverse([1,2,3,4,5,6]))

def revitup(list):
    left = 0
    right = len(list) - 1
    while left < right:
        list[left], list[right] = list[right], list[left]
        left += 1
        right -= 1
    return list
print(revitup([1,2,3,4,5,6]))

def reverseArray(array):
    new_array = []
    for i in range(len(array)-1, -1, -1):
        new_array.append(array[i])
    return new_array
print(reverseArray([1,2,3,4,5]))