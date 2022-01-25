"""Dada una lista con enteros, retornar el numero que esta duplicado,
si ningun numero está duplicado retornar None"""

def find_duplicate(nums):
	seen = []
	for num in nums:
		if num in seen:
			return num
		seen.append(num)
	return None

print(find_duplicate([1,2,3,4,5,3,7])) # 3 
print(find_duplicate([1,2,8,4,5,3,7])) # None 