# Pedindo que o usuário informe a palavra desejada e armazenando-a
palavra = input("Digite uma palavra: ")

# Pedindo ao usuário a posição que ele deseja referente a palavra escolhida
posicao = int(input("Em que posição deseja imprimir essa palavra? "))
# Imprimindo na tela a letra que está na posição indicada pelo usuário
print("\nA letra que está na posição informada é: " + palavra[posicao])
# Imprimindo na tela o restante da palavra apartir da posição informada pelo usuário
print("O restante da palavra apartir da posição informada ficará: " + palavra[posicao:])

# Imprime os caracteres nos índices pares
print("\nAs letras que estão nas posições pares são: " + palavra[::2])
# Imprime os caracteres nos índices ímpares
print("As letras que estão nas posições ímpares são: " + palavra[1::2])

# Imprime os valores concatenados da palavra informada
print("\nOs intervalos concatenados pares e ímpares são:")
print(palavra[0] + palavra[1])
print(palavra[2] + palavra[3])
print(palavra[4] + palavra[5])
