arquivo = open('ex4.txt', 'r');
par1 = []
par2= []
parNum1 = []
parNum2 = []
paresAtrib = 0
paresAtrib2 = 0

for linha in arquivo:
  linha = linha.replace('\n','')
  aux = linha.split(',')
  aux1 = aux[0].split('-')
  aux2 = aux[1].split('-')
  par1.append(aux1)
  par2.append(aux2)

for i in par1:
  parNum1.append(int(i[0]))
  parNum1.append(int(i[1]))

for i in par2:
  parNum2.append(int(i[0]))
  parNum2.append(int(i[1]))

for i in range(0, len(parNum1), 2):
  if parNum1[i] >= parNum2[i] and parNum1[i + 1] <= parNum2[i + 1]:
    paresAtrib += 1
  elif parNum1[i] <= parNum2[i] and parNum1[i + 1] >= parNum2[i + 1]:
    paresAtrib += 1 

print(paresAtrib) 
