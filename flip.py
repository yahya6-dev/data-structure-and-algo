def test(s):
	result  = 0
	for i in range(len(s)-1):
		if s[i] == "y" and s[i+1] == "x":
			result += 1
	return result

if  __name__=="__main__":
	print(test("xyxxxyxyy"))
