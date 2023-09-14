def test(L):
	result = []
	for i in range(len(L)-3+1):
		rest = L[i:i+3]
		res = 1
		for x in rest:
			res *= x 
		result.append(res)
	return max(result)


if __name__=="__main__":
	print(test([-10,-10,5,2]))
