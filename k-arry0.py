def kArry(n):
	if n==0: return []
	elif n == 1: return ["0","1"]

	return [x+y for x in kArry(n-1) for y in kArry(n-1)]


if __name__=="__main__":
	print(kArry(5))
