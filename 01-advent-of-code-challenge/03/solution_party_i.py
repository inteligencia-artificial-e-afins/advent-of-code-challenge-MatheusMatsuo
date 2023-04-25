import numpy as np

arquivo = open('ex3.1.txt', 'r');
prioridade = 0

for mochila in arquivo:
  meioArray = len(mochila) / 2
  auxInicial = str(np.array(mochila[:int(meioArray)]))
  auxFinal = str(np.array(mochila[int(meioArray):]))
  metadeInicial = []
  metadeFinal = []

  for letra in auxInicial:
    if letra in metadeInicial:
      print('essa letra ja existe na mochila')
    else: 
      metadeInicial.append(letra)

  for letra in auxFinal:
    if letra in metadeFinal:
      print('essa letra ja existe na mochila')
    else: 
      metadeFinal.append(letra)

  print(metadeInicial)
  print(metadeFinal)

  for i in range(len(metadeInicial)):
     for j in range(len(metadeFinal)):
       if metadeInicial[i] == metadeFinal[j]:
         if metadeInicial[i] == 'a':
           prioridade += 1
           break
         if metadeInicial[i] == 'b':
           prioridade += 2
           break
         if metadeInicial[i] == 'c':
           prioridade += 3
           break
         if metadeInicial[i] == 'd':
           prioridade += 4
           break
         if metadeInicial[i] == 'e':
           prioridade += 5
           break
         if metadeInicial[i] == 'f':
           prioridade += 6
           break
         if metadeInicial[i] == 'g':
           prioridade += 7
           break
         if metadeInicial[i] == 'h':
           prioridade += 8
           break
         if metadeInicial[i] == 'i':
           prioridade += 9
           break
         if metadeInicial[i] == 'j':
           prioridade += 10
           break
         if metadeInicial[i] == 'k':
           prioridade += 11
           break
         if metadeInicial[i] == 'l':
           prioridade += 12
           break
         if metadeInicial[i] == 'm':
           prioridade += 13
           break
         if metadeInicial[i] == 'n':
           prioridade += 14
           break
         if metadeInicial[i] == 'o':
           prioridade += 15
           break
         if metadeInicial[i] == 'p':
           prioridade += 16
           break
         if metadeInicial[i] == 'q':
           prioridade += 17
           break
         if metadeInicial[i] == 'r':
           prioridade += 18 
           break
         if metadeInicial[i] == 's':
           prioridade += 19
           break
         if metadeInicial[i] == 't':
           prioridade += 20
           break
         if metadeInicial[i] == 'u':
           prioridade += 21
           break
         if metadeInicial[i] == 'v':
           prioridade += 22
           break
         if metadeInicial[i] == 'w':
           prioridade += 23
           break
         if metadeInicial[i] == 'x':
           prioridade += 24
           break
         if metadeInicial[i] == 'y':
           prioridade += 25
           break
         if metadeInicial[i] == 'z':
           prioridade += 26    
           break 
         if metadeInicial[i] == 'A':
           prioridade += 27
           break
         if metadeInicial[i] == 'B':
           prioridade += 28
           break
         if metadeInicial[i] == 'C':
           prioridade += 29
           break
         if metadeInicial[i] == 'D':
           prioridade += 30
           break
         if metadeInicial[i] == 'E':
           prioridade += 31
           break
         if metadeInicial[i] == 'F':
           prioridade += 32
           break
         if metadeInicial[i] == 'G':
           prioridade += 33
           break
         if metadeInicial[i] == 'H':
           prioridade += 34
           break
         if metadeInicial[i] == 'I':
           prioridade += 35
           break
         if metadeInicial[i] == 'J':
           prioridade += 36
           break
         if metadeInicial[i] == 'K':
           prioridade += 37
           break
         if metadeInicial[i] == 'L':
           prioridade += 38
           break
         if metadeInicial[i] == 'M':
           prioridade += 39
           break
         if metadeInicial[i] == 'N':
           prioridade += 40
           break
         if metadeInicial[i] == 'O':
           prioridade += 41
           break
         if metadeInicial[i] == 'P':
           prioridade += 42
           break
         if metadeInicial[i] == 'Q':
           prioridade += 43
           break
         if metadeInicial[i] == 'R':
           prioridade += 44 
           break
         if metadeInicial[i] == 'S':
           prioridade += 45
           break
         if metadeInicial[i] == 'T':
           prioridade += 46
           break
         if metadeInicial[i] == 'U':
           prioridade += 47
           break
         if metadeInicial[i] == 'V':
           prioridade += 48
           break
         if metadeInicial[i] == 'W':
           prioridade += 49
           break
         if metadeInicial[i] == 'X':
           prioridade += 50
           break
         if metadeInicial[i] == 'Y':
           prioridade += 51
           break
         if metadeInicial[i] == 'Z':
           prioridade += 52    
           break  

print(prioridade)      
