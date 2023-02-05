def runLengthEncoding(string):
    current_letter = string[0]
    current_count = 0
    encoded_string = ""
    for i in string:
        if current_count == 9:
            encoded_string += str(current_count)
            encoded_string += current_letter
            current_letter = i
            current_count = 0
        if i == current_letter:
            current_count+=1
        else:
            encoded_string += str(current_count)
            encoded_string += current_letter
            current_letter = i
            current_count = 1
    encoded_string += str(current_count)
    encoded_string += current_letter
    return encoded_string

print(runLengthEncoding("AAAAAAAAAAAAABBCCCCDD"))

