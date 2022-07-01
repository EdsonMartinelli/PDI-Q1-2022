# ATENÇÃO COM AS ENTRADAS DE DADOS COM O COMANDO input()
# ATENÇÃO COM AS SAÍDAS DE DADOS COM O COMANDO print()
# Não esquecer de importar as bibliotecas, por exemplo:
import numpy as np
import cv2

def imprimirImagem(m): # função para imprimir a matriz
  [l,c] = m.shape
  st = ''
  for i in range(l):
    for j in range(c):
      st += str(m[i][j]) + ' '
    st += '\n'
  return st

def lerImagem(): # função para ler imagem de tamanho aleatório
  f = []
  ler_linha = input()
  while ler_linha: # até achar uma linha vazia
    f.append([int(i) for i in ler_linha.split(' ') if i])
    ler_linha = input()
  return np.array(f).astype('uint8')
 
h = lerImagem()
kernel = np.array((h), np.uint8)
img = lerImagem()

output = cv2.dilate(cv2.erode(img, kernel), kernel)
print(imprimirImagem(output)) 