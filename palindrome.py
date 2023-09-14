def test(number):
	l = list(str(number))
	r = l.copy()
	r.reverse()
	for i in range(len(l)):
		if r[i] != l[i]:
			return False
	return True

if __name__=="__main__":
	print(test(121))
	print(test(888))
	print(test(678))
