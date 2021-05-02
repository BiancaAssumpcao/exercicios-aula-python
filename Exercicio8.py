dia = int(input("Informe o dia que você nasceu: "))
mes = int(input("Informe o mês que você nasceu com dois dígitos: "))
ano = int(input("Informe o ano que você nasceu: "))

if (dia < 1) or (dia > 30):
    print()
    print("A data não é válida pois o dia informado está incorreto, deve estar entre 1 e 30.")
elif (mes < 1) or (mes > 12):
    print()
    print("A data não é válida pois o mês informado está incorreto, deve estar entre 1 e 12.")
elif ano > 2021:
    print()
    print("A data não é válida pois o ano informado é maior que o atual.")
else:
    print()
    print("A data informada é válida: " + str(dia) + "/" + str(mes) + "/" + str(ano))
