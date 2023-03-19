import math
def binarySearch(array, target):
    return binarySearchHelp(array, target, 0, len(array) - 1)

def binarySearchHelp(array, target, left_pointer, right_pointer):
    if left_pointer > right_pointer:
        return -1
    middle = math.floor((left_pointer + right_pointer) / 2)
    possible_match = array[middle]
    if target == possible_match:
        return middle
    elif target < possible_match:
        return binarySearchHelp(array, target, left_pointer, middle - 1)
    else:
        return binarySearchHelp(array, target, middle + 1, right_pointer)

print(binarySearch([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 33))