def caesarCipherEncryptor(string, key):
    place = 97
    output = ""
    for i in string:
        place = ord(i)
        for j in range(key):
            place+=1
            if place > 122:
                place = 97
                print(place)
        output += chr(place)
    return output
print(caesarCipherEncryptor("xyz",2))