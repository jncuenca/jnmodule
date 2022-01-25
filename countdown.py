"""Dado un numero retornar una lista conteniendo el mismo numero y sus predecesores hasta 1"""

def countdown(num):
	if num < 1:
		return []

	arr = countdown(num - 1)
	arr.insert(0, num)

	return arr

print(countdown(5)) #[5, 4, 3, 2, 1]