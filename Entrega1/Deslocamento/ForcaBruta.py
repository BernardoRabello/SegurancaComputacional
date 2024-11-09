from Shift import shiftCipher


cipherText = "kvjkv kvjkv kvjkreuf jlgvi kvjkv svieriuf drelvcr rsrtroz jljyz"

for i in range(1, 27):
    print(f"Chave: {i}")
    print(shiftCipher(cipherText, -i))
    input()
