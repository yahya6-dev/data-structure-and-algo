import matplotlib.pyplot as plt
import time

def test(L,x):
	i = 0
	start = time.time()
	while i < len(L):
		if L[i] == x:
			print(i)
			return i,time.time()-start
		i += 1
def test_case():
	L = [i for i in range(100000) ]
	i,t = test(L,99999)
	print("using linear search",t,i)
	start = time.time()
	result = L.index(99999)
	end = time.time()-start
	print("using index",end,result)

test_case()
