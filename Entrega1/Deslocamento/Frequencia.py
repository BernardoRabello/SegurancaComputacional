from Shift import shiftCipher


cipherText = '''vd 2016 tfcfhlvz tfdf ldr urj dvkrj uf ref "rgiveuvi r wrqvi ld sfd eyfhlv", drj wfz jh ef wzerc uv 2018 hlv wzercdvekv wzq ld eyfhlv tfd trir v jrsfi uv eyfhlv.
ld girkf hlv vl gvejvz "vl grxrizr gfi zjjf vd ld ivjkrlirekv. 
erf grxrizr dlzkf trif, drj grxrizr". 
v tfejzuvireuf dvlj krcvekfj xrjkifeidztfj, gir dzd zjjf wfz ldr srzkr tfehlzjkr, hlv jh wfz gfjjbmvc gfihlv vl dv vdgveyvz dlzkf drzj uf hlv efj refj rekvizfivj. 
vd ld dyj vl wzq drzj eyfhlvj (v kvekrkzmrj uv eyfhlvj) uf hlv r jfdr uv kfurj rj kvekrkzmrj ufj ufzj refj rekvizfivj. 
vl rgiveuz vdgziztrdvekv hlv r ivgvkzvrf tfejkrekv x ld zdgfikrekv ypszkf grir rgiveuvidfj r wrqvi rcxf hlv vozxv kxteztr, krc tfdf vjtivmvi... 
hlv x ldr urj dzeyrj dvkrj uv 2019 :)'''

ocorr = {}
for i in range(26):
    letra = chr(i+97)
    ocorr[letra] = cipherText.count(letra)

ordem = sorted(ocorr, key = lambda x : ocorr[x], reverse = True)


#Letras mais comuns da lingua portuguesa
frequencia = ["a", "e", "o", "s", "i", "r", "d", "n", "t", "c", "m", "u", "p", "l", "g", "v", "b", "f", "q", "h", "j", "z", "x", "k", "w", "y"]


for i in frequencia:
    chave = ord(ordem[0]) - ord(i)
    print(f"{ordem[0]} = {i}  -->  Chave {chave}: ")
    print(shiftCipher(cipherText, -chave))
    input()
