def test(L):
	L = "".join([str(x) for x in L])
	L=sorted(L)
	L.reverse()
	L = "".join(L)
	print(L)
	return int(L)

if __name__=="__main__":
	print(test([10,7,76,415]))
