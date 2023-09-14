def reverse_list(L):
	if len(L) <= 0:
		return []
	return [L.pop(-1)] + reverse_list(L)

if __name__=="__main__":
	print(reverse_list([0,12,32,2,4,242]))	
