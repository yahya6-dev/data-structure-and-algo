def test(A):
	L = A.copy()
	L = sorted(L,key = lambda x: len(x))
	max = L[-1]
	min  = L[0]
	maxIndex = A.index(max)
	m = len(max)-len(min)
	result = []
	for i in range(m):
		result.append(max[i])
	max = max[m:] 
	L = A
	L[maxIndex] = max
	print(L)
	for i in range(len(L)):
		for j in range(len(L[0])):
			if L[i][j] not in result:
				result.append(L[i][j])
	return result

if __name__=="__main__":
	L = [[1,7,3],[2,1,6,7,9],[3,9,5]]
	print(test(L))
