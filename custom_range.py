def custom_range(n,result=[]):
	if n <= 0:
		return 
	else:
		result.append(n-1)
		return custom_range(n-1,result)

if __name__=="__main__":
	result = []
	custom_range(10,result)
	print(result)
