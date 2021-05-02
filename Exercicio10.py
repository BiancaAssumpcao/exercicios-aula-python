# Soma de todos os números pares dentro da sequência indicada pelo usuário
num_inicial = int(input("Digite um número para dar início a sequência: "))
num_final = int(input("Digite um número para dar fim a sequência: "))

soma = 0
if( num_inicial % 2 != 0 ):
  num_inicial += 1

while( num_inicial <= num_final ):
  soma = soma + num_inicial
  num_inicial += 2

print()
print("A soma de todos os números pares dentro da sequência indicada é: " + str(soma))
