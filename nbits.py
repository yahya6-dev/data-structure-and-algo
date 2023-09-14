def check(a,b):
	a1 = ''
	b1 = ''
	for e in bin(a):
		if e == '1':
			a1 += e
	for e in bin(b):
		if e == "1":
			b1 += e
	print(a1,b1)
	return a1 == b1

def test(n):
	for b in range(n+1,n*10):
		if check(n,b):
			return b

if __name__=="__main__":
	print(test(6))
