def firstDuplicateValue(array):
    nums = {}
    for i in array:
        print(nums)
        if i in nums:
            return i
        if i not in nums:
            nums[i] = 1
    return -1
print(firstDuplicateValue([2, 1, 5, 3, 3, 2, 4]))