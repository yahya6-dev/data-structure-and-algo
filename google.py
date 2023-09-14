def test(W,S):
	result = []
	n = len(W)
	for i in range(len(S)+1-n):
		if W == S[i:i+n] or W[::-1] == S[i:i+n]:
			print(S[i+n:i:-1])
			result.append(i)
		print(i)
	return result


if __name__=="__main__":
	print(test("ab","abxaba"))
