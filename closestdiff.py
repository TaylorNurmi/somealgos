import math
def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    diff = math.inf
    answer = []
    for i in range(len(arrayOne)):
        for j in range(len(arrayTwo)):
            if arrayOne[i] > arrayTwo[j]:
                current_diff = arrayOne[i] - arrayTwo[j]
            else:
                current_diff = arrayTwo[j] - arrayOne[i]
            if current_diff < diff:
                diff = current_diff
                answer = [arrayOne[i], arrayTwo[j]]
    return answer
print(smallestDifference([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17]))