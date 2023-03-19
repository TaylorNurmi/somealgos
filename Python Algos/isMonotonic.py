def isMonotonic(array):
    if len(array) <= 1:
        return True
    for i in range(len(array)-1):
        if array[i] < array[i+1]:
                for i in range(len(array)-1):
                    if array[i] > array[i+1]:
                        return False
                return True
        elif array[i] > array[i+1]:
            for i in range(len(array)-1):
                if array[i] < array[i+1]:
                    return False
            return True
    return True

print(isMonotonic([1, 1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 7, 9, 10, 11]))