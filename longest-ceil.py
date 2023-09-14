outcomes = []
def check(L,i,A):
	if L:
		item = L.pop()
	else: return A
	if i <= 0:
		connected = item[i:i+2]
	elif i >= len(item):
		connected = item[i-1:]
	else:
		connected = item[i-1:i+2]
	ones = list(enumerate(connected))
	ones = list(filter(lambda x: x[1] == 1,ones))
	if ones:
		A[0]+=1
		for one in ones:
			return check(L,one[i],A)
	else:
		return A
def main(L):
	step = 0
	while step < len(L):
		for i,x in enumerate(L.pop()):
			if x:
				outcomes.append(check(L,i,[1]))
		step += 1
	return sorted(outcomes)[-1][0]

if __name__=="__main__":
	print(main([[1,1,0,0,0],
		[0,1,1,0,0], 
		[0,0,1,0,1],
		[1,0,0,0,1],
		[0,1,0,1,1]]))
