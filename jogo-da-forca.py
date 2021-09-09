#Hangman Game in Portuguese
#code by Anderson Freixo - 2019

"""Jogo da Forca (Hangman)
Esta é uma implementação bastante simples de um Jogo da Forca em Python,
com menos de 50 linhas de código.
Veja o passo-a-passo para a criação do jogo aqui:
https://amadorprograma.wordpress.com/2019/02/25/criando-um-jogo-da-forca-em-python/
"""

__author__ = "Anderson Freixo <anderson.freixo@gmail.com>"

from random import choice

vocabulario = ["esquistossomose", "naftalina", "ribonucleico", "idiossincratico", "fagocitose", "quinquagesimo"]

palavra = choice(vocabulario)

print("JOGO DA FORCA 1.0\n")
print("Bem vindo ao JOGO DA FORCA. Boa sorte!\n")

chances = 6
alfabeto = list("abdcefghijklmnopqrstuvwxyz")
tentativas = []

while True:
	print(tentativas)
	print("Chances: ",chances)

	for letra in palavra:
		if letra in tentativas:
			print(letra, end = ' ')
		else:
			print('_', end= ' ')

	palpite = input("\nDigite seu palpite ou 'SAIR' para sair do programa!").lower()
	if palpite == "sair":
		break	
	elif palpite not in alfabeto or palpite == '':
		print("Hein!? Fala direito! Isso não é uma letra!")
		continue	
	elif palpite in tentativas:
		print("Você é desmemoriado ou o quê!? Você já tentou essa letra. Tente outra!")
		continue
	tentativas.append(palpite)
	if palpite in palavra:
		print("ACERTÔ, MIZERAVI!")
	else:
		print("Errou feio, errou rude!")
		chances-=1
	if chances == 0:
		print("Perdeu, pivete! Game over!!! >:)")
		break
	elif set(palavra).issubset(set(tentativas)):
		print("Parabéns, você acertou! Weeee are the champions, my frieeeend!")
		break
