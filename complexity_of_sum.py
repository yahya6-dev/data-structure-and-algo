import time

def test(L):
	return L[0]+test(L[1:]) if len(L) > 0 else 0

def test_case():
	L = [x for x in range(600)]
	start = time.time()
	result = test(L)
	end = time.time()-start
	print("time for summing 100000 items using recursion",end)
	start = time.time()
	result = sum(L)
	end = time.time() - start
	print("time for summing 100000 using builtin sum",end)

if __name__=="__main__":
	test_case()
