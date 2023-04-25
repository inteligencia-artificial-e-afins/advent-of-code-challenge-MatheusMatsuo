arquivo = open('jaquempo.txt', 'r');
adversario = []
eu = []
pontos = 0

for linha in arquivo:
  adversario.append(linha[0])
  eu.append(linha[2])

for jogada in range(len(adversario)):
    if eu[jogada] == "X":
      if adversario[jogada] == "A":
        pontos += 0 + 3
      elif adversario[jogada] == "B":
        pontos += 0 + 1
      else:
        pontos += 0 + 2

    if eu[jogada] == "Y":
      if adversario[jogada] == "A":
        pontos += 3 + 1
      elif adversario[jogada] == "B":
        pontos += 3 + 2
      else:
        pontos += 3 + 3

    if eu[jogada] == "Z":
      if adversario[jogada] == "A":
        pontos += 6 + 2
      elif adversario[jogada] == "B":
        pontos += 6 + 3
      else:
        pontos += 6 + 1

print(pontos)
