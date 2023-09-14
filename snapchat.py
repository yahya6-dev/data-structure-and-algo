def test(L):
	result = 0
	j = 0
	while j < len(L)-1:
		for i in range(j+1,len(L)):
			s = L[j]
			s2 = L[i]
			if  set(range(s[0],s[1])) & set(range(s2[0],s2[1])):
				result += 1
		j += 1
	return result


if __name__=="__main__":
	intervals = [(30,70),(0,50),(60,150)]
	print(test(intervals))
