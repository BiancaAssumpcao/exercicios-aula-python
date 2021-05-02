dicionario = {}

dicionario["Nome"] = input("Digite o seu nome: ")
dicionario["UltimoNome"] = input("Digite seu último nome: ")
dicionario["Idade"] = int(input("Digite sua idade: "))
dicionario["Curso"] = input("Digite o nome do seu curso: ")
dicionario["Endereco"] = input("Digite seu endereço: ")

# a) Imprima o dicionário completo
print()
print(dicionario.items())

# b) Imprima cada um dos 5 itens separadamente
print("\nNome: " + str(dicionario["Nome"]))
print("Último Nome: " + str(dicionario["UltimoNome"]))
print("Idade: " + str(dicionario["Idade"]))
print("Curso: " + str(dicionario["Curso"]))
print("Endereço: " + str(dicionario["Endereco"]) + "\n")

# c) Exclua a chave CURSO do dicionário
dicionario.pop("Curso")

# d) Altere o ULTIMO NOME para Lopes
dicionario["UltimoNome"] = "Lopes"

# e) Imprima novamente o dicionário completo
print(dicionario.items())

# f) Imprima apenas o endereço
print("\nEndereço: " + str(dicionario["Endereco"]) + "\n")

# g) Crie uma cópia do dicionário e altere Nome e Idade
dicionario2 = dicionario.copy()
dicionario2["Nome"] = "Bianca"
dicionario2["Idade"] = 20

# h) Imprima o segundo dicionário completo
print(dicionario2.items())
