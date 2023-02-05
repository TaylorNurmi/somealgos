def moveElementToEnd(array, toMove):
    for left in range(len(array)):
        if array[left] == toMove:
            for right in range(len(array)-1, left, -1):
                if right <= left:
                    return array
                if array[right] != toMove:
                    array[left], array[right] = array[right], array[left]
    return array
print(moveElementToEnd([2, 1, 2, 2, 2, 3, 4, 2], 2))