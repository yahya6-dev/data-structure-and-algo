def test(L):
	if len(L) == 1:
		return True
	return L[0] < L[1] and  test(L[1:])

if __name__=="__main__":
	print(test([1,23,2,24,25,26]))
