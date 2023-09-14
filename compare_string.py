def compare_lt(str1,str2):
	r1 = sum([ord(x) for x in str1])
	r2 = sum([ord(x) for x in str2])
	return r1 < r2
