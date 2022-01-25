"""Genera cadena de string specificando 
- longitud de cadena deseada 
- cantidad de cadenas a ser generada
- debe contener caracteres en mayuscula
- debe contener caracteres en minuscula
- debe contener numeros
- debe contener simbolos

Ejemplo:
generate_random(40, 10, True, True, False, True)
"""

import random

def generate_random(length, amount, upper, lower, nums, syms):
	uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	lowercase_letters = uppercase_letters.lower()
	numbers = "1234567890"
	symbols = "#$%&/(){}[]:_.*-"

	upper, lower, nums, syms = upper, lower, nums, syms
	length = length
	amount = amount

	all_chars=""

	if upper: all_chars += uppercase_letters
	if lower: all_chars += lowercase_letters
	if nums: all_chars += numbers
	if syms: all_chars += symbols



	for i in range(amount):
		password = "".join(random.sample(all_chars, length))
		print(password)	
		print("-----------------------------")


generate_random(40, 10, True, True, False, True)