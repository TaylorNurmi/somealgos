def findThreeLargest(array):
    large = []
    if len(array) > 3:
        for i in range(len(array)):
            if len(large) < 3:
                large.append(array[i])
                large.sort()
            if array[i] > large[0]:
                large[0] = array[i]
                large.sort()
        return large
    else:
        array.sort()
        return array

print(findThreeLargest([10, 5, 9, 10, 12]))

