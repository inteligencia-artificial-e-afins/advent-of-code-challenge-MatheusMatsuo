arquivo = open('mario1.txt', 'r');

caloriasPorElfo = []
aux = 0
caloriasMaioresTresElfos = 0

for linha in arquivo:
  if linha != '\n':
    aux = aux + int(linha)
  else:
    caloriasPorElfo.append(aux)
    aux= 0

for i in range(3):
      maiorCaloria = max(caloriasPorElfo)
      caloriasMaioresTresElfos += maiorCaloria
      caloriasPorElfo.remove(maiorCaloria)

print("A soma de calorias dos 3 maiores elfos é de " + str(caloriasMaioresTresElfos) + " calorias")
