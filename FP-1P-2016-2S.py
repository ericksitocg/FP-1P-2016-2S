#Autor Erick Humberto Cordova Gavilanes
import numpy as np
import random as rd
#Tema 1

L_vocales = ['a', 'e', 'i', 'o', 'u']
L_consonantes = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

texto = input("Ingrese un texto: ").lower()
contador_palabra = 0

texto = texto.replace("."," ")

L_pal = texto.split(" ")
for palabra in L_pal:
	contador_vocales = 0
	contador_consonantes = 0

	for letra in palabra:
		if letra in L_vocales:
			contador_vocales+=1
		elif letra in L_consonantes:
			contador_consonantes+=1
	if contador_vocales==contador_consonantes and contador_vocales!=0:
		contador_palabra+=1

print("el texto tiene %d palabras"%contador_palabra)