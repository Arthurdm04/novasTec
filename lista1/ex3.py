# Faça um programa que calcule a distância entre dois pontos no plano cartesiano.
import math

xA = int(input('Digite a coordenada x do ponto A: '))
yA = int(input('Digite a coordenada y do ponto A: '))

xB = int(input('Digite a coordenada x do ponto B: '))
yB = int(input('Digite a coordenada y do ponto B: '))

distancia = math.sqrt((xB - xA)**2 + (yB - yA)**2)

print('O resutlado é {:.2f}'.format(distancia))
