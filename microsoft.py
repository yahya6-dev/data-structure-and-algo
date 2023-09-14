def test(L,w):
	for i in range(len(L)):
		if ''.join(L[i]) == w:
			print(L[i])
			return True
		r = ''
		for j in range(len(L[0])):
			r +=  L[j][i]
		print(r)
		if r == w:
			return True


if __name__=="__main__":
	L = [['F','A','C','I'],['O','B','Q','P'],['A','N','O','B'],['M','A','S','S']]
	print(test(L,"FOAM"),"FOAM")
	print(test(L,"MASS"),"MASS")
