def length_of_string(x):
	if x == '':
		return 0
	else:
		return 1 + length_of_string(x[1:])

if __name__=="__main__":
	print(length_of_string("hornet Is Your King!"))
