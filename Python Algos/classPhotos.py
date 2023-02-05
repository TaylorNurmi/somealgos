def classPhotos(redShirtHeights, blueShirtHeights):
    redShirtHeights.sort()
    blueShirtHeights.sort()
    big = []
    small = []
    if redShirtHeights[0] > blueShirtHeights[0]:
        big = redShirtHeights
        small = blueShirtHeights
    else:
        big = blueShirtHeights
        small = redShirtHeights
    for i in range(len(big)):
        if big[i] <= small[i]:
            return False
    return True
print(classPhotos([5, 8, 3, 3, 4], [6, 9, 2, 4, 5]))