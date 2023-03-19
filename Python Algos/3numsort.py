def threeNumberSort(array, order):
    for i in range(len(array)):
        if array[i] == order[2]:
            for j in range(len(array) - 1, i, -1):
                if array[j] != order[2]:
                    array[j], array[i] = array[i], array[j]
                    break
        if array[i] == order[1]:
            for j in range(len(array) - 1, i, -1):
                if array[j] == order[0]:
                    array[j], array[i] = array[i], array[j]
                    break
    return array

print(threeNumberSort([1, 0, 0, -1, -1, 0, 1, 1], [0, 1, -1]))