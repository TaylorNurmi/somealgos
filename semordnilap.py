def semordnilap(words):
    semordnilaps = []
    for i in range(len(words)):
        for j in range(i+1,len(words)):
            if words[i] == words[j][len(words[j])::-1]:
                semordnilaps.append([words[i], words[j]])
    return semordnilaps
print(semordnilap(["diaper", "abc", "test", "cba", "repaid"]))

