arquivo = open('ex6.txt', 'r');
arrayPacote = []
for linha in arquivo:
  pacote = linha


for caractere in list(pacote):
  arrayPacote.append(caractere)

tamanhoPacote = len(arrayPacote)

for i in range(tamanhoPacote):
  if i < (tamanhoPacote - 3):
      if arrayPacote[i] != arrayPacote[i + 1] and arrayPacote[i] != arrayPacote[i + 2] and arrayPacote[i] != arrayPacote[i + 3] and arrayPacote[i + 1] != arrayPacote[i + 2] and arrayPacote[i + 1] != arrayPacote[i + 3] and arrayPacote[i + 2] != arrayPacote[i + 3]:
        primeiroMarcador = i + 4
        break
         

print(primeiroMarcador)
