import random

print("O computador pensou em um número entre 0 e 100, você é capaz de advinhar?")
print("Você terá 3 tentativas! BOA SORTEE!!!")
sorteio = random.randint(0, 100)

cont = 0
while (cont < 3):
    print()
    num = int(input("Digite o seu palpite: "))
    if num == sorteio:
        print("Parabéns, o número pensado pelo computador foi {}, o mesmo do seu!!!".format(sorteio))
        break

    elif (sorteio == num + 1) or (sorteio == num + 2) or (sorteio == num + 3):
        print("Está quente, mas ainda não é número correto!")

    elif (sorteio == num - 1) or (sorteio == num - 2) or (sorteio == num - 3):
        print("Está quente, mas ainda não é número correto!")

    else:
        print("Opa, está frio, passou longe!")

    cont = cont + 1

    if cont == 3:
        print()
        print("Que pena, suas tentativas acabaram! O número pensado foi {}.".format(sorteio))
