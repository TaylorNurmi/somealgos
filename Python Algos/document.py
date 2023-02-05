characters = "Bste!hetsi ogEAxpelrt x "
document = "AlgoExpert is the Best!"

def generateDocument(characters, document):
    characters = list(characters)
    document = list(document)
    for i in range(len(document)):
        for j in range(len(characters)):
            if document[i] == characters[j]:
                document[i], characters[j] = 0, None
    answer = ''.join([str(n) for n in document])
    if answer.isdigit() or answer == '':
        return True
    else: 
        return False
print(generateDocument(characters, document))