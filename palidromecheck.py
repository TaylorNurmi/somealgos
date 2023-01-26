import math

def isPalidrome(string):
    start_of_list = string[:math.floor(len(string)/2)]
    end_of_list = string[math.ceil(len(string)/2):]
    reverse_end = list(end_of_list)
    string_end = ""
    for i in range(len(reverse_end)-1, -1, -1):
        string_end+= reverse_end[i]
    if len(string) == 1:
        return True
    elif  start_of_list == string_end:
        return True
    else:
        return False

print(isPalidrome("kabcdcbak"))