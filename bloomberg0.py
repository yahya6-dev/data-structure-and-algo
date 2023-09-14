def test(s,s1):
	s = list(set(list(s)))
	s1 = list(set(list(s1)))
	return len(s1) == len(s)

if __name__=="__main__":
	print(test("abc","bcd"))
	print(test("foo","bar"))
