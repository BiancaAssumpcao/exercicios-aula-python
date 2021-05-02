# Votação
cand1 = 0
cand2 = 0
cand3 = 0
cand4 = 0
nulo = 0
branco = 0

print()
print("------------------------------------------------------------------------------------")
print("Segue abaixo a lista dos candidatos dessa eleição e o seu respectivo número: ")
print()
print("     Candidato número 1 -> Lula do partido PT -- DÍGITO 1")
print("     Candidato número 2 -> Bolsonaro do partido PSDB -- DÍGITO 2")
print("     Candidato número 3 -> Marina do partido REDE -- DÍGITO 3")
print("     Candidato número 4 -> Ciro do partido PDT -- DÍGITO 4")
print("     Para Votos Nulos -- DÍGITO 5")
print("     Para Votos em Branco -- DÍGITO 6")
print("     Para encerrar a votação -- DÍGITO 0")
print("------------------------------------------------------------------------------------")
print()

while True:
    voto = int(input("Informe o número do seu candidato (ou digite '0' para finalizar): "))
    if voto == 0:
        break
    if voto == 1:
        cand1 += 1
    elif voto == 2:
        cand2 += 1
    elif voto == 3:
        cand3 += 1
    elif voto == 4:
        cand4 += 1
    elif voto == 5:
        nulo += 1
    elif voto == 6:
        branco += 1
    else:
        print("Número inválido, informe um número correto!")

print()
print("O total de votos para o candidato número 1 (Lula) foi: "+ str(cand1))
print("O total de votos para o candidato número 2 (Bolsonaro) foi: "+ str(cand2))
print("O total de votos para a candidata número 3 (Marina) foi: "+ str(cand3))
print("O total de votos para o candidato número 4 (Ciro) foi: "+ str(cand4))
print("O total de votos nulos foi: " + str(nulo))
print("O total de votos em branco foi: " + str(branco))
