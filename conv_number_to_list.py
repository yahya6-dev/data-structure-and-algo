def ret_number_to_lst(arg):
	"""this function assume you pass it 
	 a number then it return a list consisted of its 
	 digits like 10 return [1,0]  1222 [1,2,2,2] 
	 in O(1) complexity
	"""
	if arg == 0: return [0]
	l = []
	left = arg // 10 if arg >= 10 else   arg % 10
	right = arg % 10 if arg >= 10 else 10 % arg
	left =  arg if (arg < 10 and left == 10) else left
	l.append(left)
	if l[0] >= 10:
		left = ret_number_to_lst(l[0])
		l = left
	if arg  >= 10:
		l.append(right)
	return l



if __name__=="__main__":
	for i in range(1000):
		print(ret_number_to_lst(i))
