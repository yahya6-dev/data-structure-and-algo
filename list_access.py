import time

def test(size):
	L = []
	for i in range(size):
		L.append(i*2)
	times = []
	i = 0
	while i < len(L):
		start = time.time()
		L[i] = L[i]*2
		end = time.time()
		times.append(end-start)
		i += 1
	return times


