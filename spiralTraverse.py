def spiralTraverse(array):
    result = []
    spiral_fill(array, 0, len(array) - 1, 0, len(array[0]) - 1, result)
    return result

def spiral_fill(array, startRow, endRow, startCol, endCol, result):
    if startRow > endRow or startCol > endCol:
        return

    for col in range(startCol, endCol + 1):
        result.append(array[startRow][col])
    for row in range(startRow + 1, endRow + 1):
        result.append(array[row][endCol])

    if startRow < endRow:
        for col in reversed(range(startCol, endCol)):
            result.append(array[endRow][col])
    if startCol < endCol:
        for row in reversed(range(startRow + 1, endRow)):
            result.append(array[row][startCol])

    if startRow == endRow or startCol == endCol:
        return

    spiral_fill(array, startRow + 1, endRow - 1, startCol + 1, endCol - 1, result)

print(spiralTraverse([
[1, 2, 3, 4], 
[12, 13, 14, 5], 
[11, 16, 15, 6], 
[10, 9, 8, 7]]))