"""Dada una palabra, construye la palabra palindrome si es un palindrome
Pasos:
palabra_dada = "momomoomomo"
1-crear un dict con key=caracter_de_palabra & valor=cantidad_apariciones.
En este caso se encuentran 5 m's y 6 o's
{
	'm': 5,
	'o': 6,
}
2- recorrer los keys y values, en este caso haran 2 iteraciones
 *si el value del key es Par se agrega al palidrome su mitad de apariciones
 *si el value del key es Impar se guarda el key como un caracter impar y se agrega al palidrome su mitad de apariciones
	palindrome = mmooo
	odd_char = m
3- Se retorna (palindrome + odd_char + reverse_palimdrome) => (mmooo + m + ooomm)
"""

def palidrome(word):
	count_char = dict()
	for c in word:
		if not count_char.get(c): count_char[c] = 0
		count_char[c] += 1

	odd_char = ""
	palidrome = ""

	for c, cnt in count_char.items():
		if cnt % 2 == 0:
			palidrome += c * (cnt//2)
		elif odd_char == "":
			odd_char = c 
			palidrome += c * (cnt//2)
		else: 
			return None

	return palidrome + odd_char + palidrome[::-1]

print(palidrome("momomoomomo")) #mmooomooomm
print(palidrome("momo")) #moom
print(palidrome("momomo")) #None




