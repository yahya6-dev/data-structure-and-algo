def select(seq,start):
	minIndex = start
	for i in range(start+1,len(seq)-1):
		if seq[i] > seq[minIndex]:
			minIndex = i
	return minIndex

def sort(seq):
	for i in range(len(seq)):
		minIndex = select(seq,i)
		temp = seq[i]
		seq[i] = seq[minIndex]
		seq[minIndex] = temp