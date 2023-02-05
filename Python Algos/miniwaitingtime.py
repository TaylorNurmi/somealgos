def minimumWaitingTime(queries):
    queries.sort()
    waitTime = 0
    totalWait = 0
    for i in range(len(queries)-1):
        waitTime += queries[i]
        totalWait += waitTime
    return totalWait
print(minimumWaitingTime([3, 2, 1, 2, 6]))