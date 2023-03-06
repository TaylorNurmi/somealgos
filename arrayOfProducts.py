def arrayOfProducts(array):
    result = []
    for i in range(len(array)):
        new_index = 1
        for j in range(len(array)):
            if j != i:
                new_index *= array[j]
        result.append(new_index)
    return result


print(arrayOfProducts([5, 1, 4, 2]))