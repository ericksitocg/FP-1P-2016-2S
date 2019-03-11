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

#Tema 2
sur = ['LosEsteros','Pradera','RiocentroSur']
centro = ['Bahia', 'Malecon2000','MaleconSalado']
norte = ['MallDelSol', 'CityMall','RiocentroNorte']

futbol = ['zapatos-Adidas', 'zapatos-Nike','rodilleras-Reebok']
natacion = ['short-Nike', 'gafasPiscina-Swingo','aletas-Speedo']

L_tiendas = sur + centro + norte
L_categorias = futbol + natacion

#Se genera una matriz de numeros aleatorios para poder realizar el ejercicio
M = np.random.randint(5,100,(len(L_tiendas),len(L_categorias)))

"""
1. La categoría que tiene mayor cantidad de ventas y su valor. Por ejemplo:
	a. Si ambas tuvieran la misma cantidad de ventas, muestre: Iguales: 12348.37
	b. Si fútbol tiene más ventas muestre: Fútbol tiene más ventas: 15000.95
"""

ventas_categorias = M.sum(axis=0)

ventas_futbol = ventas_categorias[0:len(futbol)]
ventas_natacion = ventas_categorias[len(futbol):]

total_ventas_futbol = ventas_futbol.sum()
total_ventas_natacion = ventas_natacion.sum()

if total_ventas_futbol >total_ventas_natacion:
	print("Futbol tiene mas ventas: %.2f"%total_ventas_futbol)
elif total_ventas_futbol < total_ventas_natacion:
	print("Natacion tiene mas ventas: %.2f"%total_ventas_natacion)
else:
	print("Iguales: %.2f"%total_ventas_natacion)
"""
2. La tienda que más ha vendido. Por ejemplo:
Bahía, con un monto de 8238.93
"""

ventas_tiendas = M.sum(axis=1)
tienda_mas_vendida = L_tiendas[ventas_tiendas.argmax()]
print("%s con un monto de %.2f"%(tienda_mas_vendida,ventas_tiendas.max()))

"""
3. La tienda que más ha vendido en el norte. Por ejemplo:
CityMall con 1345.90
"""

ventas_tiendas_norte = ventas_tiendas[len(sur) + len(centro): ]
tienda_mas_vendida_norte = norte[ventas_tiendas_norte.argmax()]
print("%s con un monto de %.2f"%(tienda_mas_vendida_norte,ventas_tiendas_norte.max()))

"""
4. El artículo más vendido en el sur. Por ejemplo:
zapatos-Nike
"""

ventas_tiendas_sur = ventas_tiendas[:len(sur)]
tienda_mas_vendida_sur = sur[ventas_tiendas_sur.argmax()]
print("%s con un monto de %.2f"%(tienda_mas_vendida_sur,ventas_tiendas_sur.max()))

"""
5. El número de productos distintos que se han vendido en una tienda dada por el usuario y cuáles
son esos productos. Si la tienda no existiera, debe darle un mensaje al usuario: “Tienda no
existente”. Por ejemplo:
	Tienda: MaleconSalado
	Productos distintos vendidos: 3
	Productos: zapatos-Adidas, zapatos-Nike, gafasPiscina-Swingo
"""