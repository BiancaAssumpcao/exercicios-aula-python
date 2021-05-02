cerveja = 75 * 2.20
macarrao = 2 * 8.73
molho = 3.45
cebola = (5.40 / 1000) * 420
alho = (30 / 1000) * 250
pao = (25 / 1000) * 450

total = cerveja + macarrao + molho + cebola + alho + pao
media = total / 5

print()
print("O total da compra ficou em: R$ {}".format(total))
print("Cada um terá que pagar: R$ {:.2f}".format(media))
