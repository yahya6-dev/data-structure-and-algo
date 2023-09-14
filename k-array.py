def appendAtBeginning(x,l):
	return [x+ elem for elem in l]


def kArray(n):
	if n==0: return []
	elif n == 1: return ["0","1"]

	return appendAtBeginning("0",kArray(n-1))+appendAtBeginning("1",kArray(n-1))


if __name__=="__main__":
	print(kArray(10))
