arquivo = open('jaquempo.txt', 'r');

adversario = []
eu = []
pontos = 0

for linha in arquivo:
  adversario.append(linha[0])
  eu.append(linha[2])

for jogada in range(len(adversario)):
    if adversario[jogada] == "A":
      if eu[jogada] == "Y":
        pontos += 6 + 2
      elif eu[jogada] == "Z":
        pontos += 0 + 3
      else:
        pontos += 3 + 1

    if adversario[jogada] == "B":
      if eu[jogada] == "X":
        pontos += 3 + 2
      elif eu[jogada] == "Y":
        pontos += 6 + 3
      else:
        pontos += 0 + 1

    if adversario[jogada] == "C":
      if eu[jogada] == "X":
        pontos += 0 + 2
      elif eu[jogada] == "Y":
        pontos += 3 + 3
      else:
        pontos += 6 + 1
print(jogada)


print(pontos)
