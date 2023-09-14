def test(L):
	result = []
	for i in range(len(L)):
		start = L[i]
		res = set()
		for j in range(i,len(L)):
			if start > L[j]:
				res.add(L[j])
				res.add(start)
				start = L[j]
			if  start < L[j]:
				res.add(L[j])
				break
		result.append(list(res))
	m = max([len(x)*min(x) for x in result if x])
	print(m)
	return m

if __name__=="__main__":
	print(test([1,3,2,5]))
	print(test([4,6,3,2,7]))
	print(test([0,1,2,3,5]))
	print(test([2,6,3,4]))
