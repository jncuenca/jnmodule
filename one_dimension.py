"""Dada una lista con anidaciones retornar una lista de una sola dimension

[3, 5, [ [3,[[8]]]]] => [3, 5, 3, 8]
"""

def one_dimension(lista):
	if lista == []: return lista
	
	elem = lista.pop(0) # remove the first element from the list and keep it into a var

	#to remove anidation
	while type(elem) is list: 
		lista = elem 
		elem = elem.pop(0)
	
	return [elem] + one_dimension(lista)

nums = [3, 5, [ [3,[[8]]]]]
print(one_dimension(nums)) # [3, 5, 3, 8]