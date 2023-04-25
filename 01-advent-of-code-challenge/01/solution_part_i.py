
arquivo = open('mario1.txt', 'r');

caloriasPorElfo = []
aux = 0

for linha in arquivo:
  if linha != '\n':
    aux = aux + int(linha)
  else: 
      caloriasPorElfo.append(aux) 
      aux = 0

print("O elfo com maior calorias tem " + str(max(caloriasPorElfo)) + " calorias")
