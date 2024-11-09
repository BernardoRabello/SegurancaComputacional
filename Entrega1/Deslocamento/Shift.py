#Cifra por deslocamento, para descriptografar basta usar a chave negativa
def shiftCipher(text, key):
    text = text.lower()
    output = ""
    for i in text:
        if i.isalpha():
            output += chr((ord(i) - 97 + key) % 26 + 97)   #Estou convertendo as letras para a sua representação ascii
        else:
            output += i
    return output



if __name__ == "__main__":
    texto = '''Teste teste testando super teste Bernardo abacaxi sushi'''
    chave = 17

    print(shiftCipher(texto, chave))

    print(shiftCipher(shiftCipher(texto, chave), -chave))