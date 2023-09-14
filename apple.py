def main(L):
	d = tuple(L)
	for i in d:
		if i == d.index(i):
			print(i)
main([0,1,2,7,6])
