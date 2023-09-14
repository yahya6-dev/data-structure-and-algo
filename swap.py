def swap(text,i=0):
	if i >= len(text)-1:
		return ''
	else:
		return text[1+i]+text[i]+swap(text,i+2)
if __name__=="__main__":
	print(swap("hornet"))
