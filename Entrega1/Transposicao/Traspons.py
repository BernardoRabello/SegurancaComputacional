#Função para criptografar usando cifra de transposição:
def transposE(text, key):
    key = key.lower()
    keySize = len(key)
    text = text.lower()
    
    keySorted = sorted(list(key))
    keyTmp = [([{keySorted[x]: x for x in range(keySize)}[y] for y in key][z], z) for z in range(keySize)]
    keyOrd = [item[1] for item in sorted(keyTmp, key = lambda x : x[0])]
    
    textPadding = text + "".join([chr(x + 97) for x in range(len(text) % keySize)])
    output = ""

    for i in keyOrd:
        for j in range(len(textPadding) // keySize):

            output += textPadding[j*keySize + i]
    
    return output

#Função para descriptografar usando cifra de transposição:
def transposD(text, key):
    key = key.lower()
    keySize = len(key)
    text = text.lower()
    
    keySorted = sorted(list(key))
    keyTmp = [([{keySorted[x]: x for x in range(keySize)}[y] for y in key][z], z) for z in range(keySize)]
    keyOrd = [item[1] for item in sorted(keyTmp, key = lambda x : x[0])]

    output = [' ' for x in text]
    
    acc = 0
    for i in keyOrd:
        for j in range(len(text) // keySize):
            output[j*keySize + i] = text[acc]
            acc += 1

    return "".join(str(element) for element in output)

    

if __name__ == "__main__":
    cifrado = transposE("pleasetransferonemilliondollarstomyswissbankaccountsixtwotwo", "megabuck")
    decifrado = transposD(cifrado, "megabuck")
    print(cifrado)
    print(decifrado)