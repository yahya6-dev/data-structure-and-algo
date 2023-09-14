def rev(L):
	accumulator = []
	for x in L:
		accumulator =  [x] + accumulator
	return accumulator

if __name__=="__main__":
	print(rev([1,232,224,2])) 
