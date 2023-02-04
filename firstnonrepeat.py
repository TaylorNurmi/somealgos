def first_non_repeating(s):
    char_count = {}
    count = -1
    for i in range(len(s)):
        if s[i] in char_count:
            char_count[s[i]][0] +=1
        else:
            char_count[s[i]] = [1,i]
    for item in char_count.items():
        count+=1
        if item[1][0] == 1:
            return item[1][1] 
    return -1

print(first_non_repeating("faadabcbbebdf"))