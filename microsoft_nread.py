def test(file,n):
	file,text = file[n:], file[:n] 
	return file,text


if __name__=="__main__":
	file = open("microsoft.py").read()
	file,text = test(file,80)
	print(text,len(text))
