def commonCharacters(strings):
    short_string = strings[0]
    in_common = []
    nums = {}
    if len(strings) == 1:
        return strings
    for string in range(len(strings)):
        if short_string > strings[string]:
            short_string = strings[string]
    for char in short_string:
        if char not in nums:
            nums[char] = 0
        else:
            continue
    for i in range(len(strings)):
        counted = {}
        for j in range(len(strings[i])):
            if strings[i][j] in nums and strings[i][j] not in counted:
                nums[strings[i][j]] += 1
                counted[strings[i][j]] = True
    for key in nums:
        if nums[key] == len(strings):
            in_common.append(key)
    return in_common


print(commonCharacters(["aa", "aa"]))