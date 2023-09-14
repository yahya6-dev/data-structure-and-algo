def reverseList(L):
	rest = []
	if L == []:
		return []
	first = [L[-1]]
	rest = reverseList(L[:-1])
	result = first + rest

	return result

if __name__=="__main__":
	print(reverseList([3,43,3434]))
