def getNthFib(n):
    arr= [0,1]
    for i in range(n):
        if i != 0:    
            arr.append(arr[i] + arr[i-1])
    return arr[n-1]
print(getNthFib(6))
