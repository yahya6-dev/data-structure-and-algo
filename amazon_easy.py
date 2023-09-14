def find_number(L):
	result = []
	for i in range(len(L)):
		if i > 0:
			if sum(L[:i+1]) not in L and  sum(L[:i+1])+1 not in L:
				return sum(L[:i+1]) + 1 
		elif sum(L[:1+i])+1 not in L:
			return sum(L[:i+1])+1


print(find_number([1,2,3,10]))
print(find_number([1,2,4,10]))
print(find_number([1,10]))
print(find_number([1,3,7,10]))
print(find_number([1,2,3,4,7]))
