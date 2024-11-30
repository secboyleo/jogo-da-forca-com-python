import random

print("JOGO DA FORCA")

vetEscondido = []
vetPalavra = []
vetSecreto = []

lista = ["testando", "dois", "jacare", "boi"]
indice = random.randint(0, len(lista) - 1)

palavraSecreta = lista[indice]
palavraEscondida = ""
palavra = ""

for i in palavraSecreta:
    palavraEscondida += "_"
    
palavra = palavraEscondida[:]

for i in palavraEscondida:
    vetEscondido.append(i)
    vetPalavra.append(i)

for i in palavraSecreta:
    vetSecreto.append(i)

while vetPalavra != vetSecreto:
    word = ""
    for i in vetEscondido:
        word += f"{i} "
    print(f"{word}\n")
        
    
    adv = input("adivinhe uma letra >>> \n")
    
    for i in range(len(palavraSecreta)):
        if adv == palavraSecreta[i]:
            vetEscondido[i] = palavraSecreta[i]
            vetPalavra[i] = palavraSecreta[i]
            
print(f"voce adivinhou a palavra {palavraSecreta}")