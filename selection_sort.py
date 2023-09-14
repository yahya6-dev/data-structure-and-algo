def select(seq,start):
	minIndex = start
	for j in range(start+1,len(seq)):
		if seq[minIndex] > seq[j]:
			minIndex = j
	return minIndex

def sort(seq):
	for i in range(len(seq)-1):
		minIndex = select(seq,i)
		temp  = seq[i]
		seq[i] = seq[minIndex]
		seq[minIndex] = temp


if __name__=="__main__":
	L = [1,23,24,2,-1,24,-9]
	sort(L)
	print(L)