def threenumsum(array, target):
    output = []
    for i in range(len(array)):
        for j in range(i+1,len(array)):
            for x in range(j+1,len(array)):
                if array[i] + array[j] + array[x] == target:
                    sums = [array[i],array[j],array[x]]
                    sums.sort()
                    output.append(sums)
    output.sort()
    return output
print(threenumsum([12, 3, 1, 2, -6, 5, -8, 6], 0))