def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    redShirtSpeeds.sort()
    blueShirtSpeeds.sort()
    maxTotal = 0
    minTotal = 0
    for i in range(len(redShirtSpeeds)):
        if redShirtSpeeds[i] >= blueShirtSpeeds[len(blueShirtSpeeds)-i-1]:
            maxTotal += redShirtSpeeds[i]
        else:
            maxTotal += blueShirtSpeeds[len(blueShirtSpeeds)-i-1]
        if redShirtSpeeds[i] >= blueShirtSpeeds[i]:
            minTotal += redShirtSpeeds[i]
        else:
            minTotal += blueShirtSpeeds[i]
    if fastest == True:
        return maxTotal
    else:
        return minTotal

print(tandemBicycle([5,5,3,9,2], [3,6,7,2,1], False))