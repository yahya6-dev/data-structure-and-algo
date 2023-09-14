import random

def partition(seq,start,stop):
	pivotIndex = start
	pivot = seq[pivotIndex]
	i = start + 1
	j = stop - 1

	while i <= j:
		while i <= j and not pivot < seq[i]:
			i += 1
		while i <= j  and pivot < seq[j]:
			j -= 1
		if i < j:
			tmp = seq[i]
			seq[i] = seq[j]
			seq[j] = tmp
			i += 1
			j -= 1
	seq[pivotIndex] = seq[j]
	seq[j] = pivot
	return j

def merge_recursively(seq,start,stop):
	if start >= stop - 1:
		return
	pivotIndex = partition(seq,start,stop)
	merge_recursively(seq,start,pivotIndex)
	merge_recursively(seq,pivotIndex+1,stop)

def quicksort(seq):
	for i in range(0,len(seq)):
		j = random.randint(0,len(seq)-1)
		tmp = seq[i]
		seq[i] = seq[j]
		seq[j] = tmp
	merge_recursively(seq,0,len(seq))


if __name__=="__main__":
	L = [-3,3,12,32,-2]
	quicksort(L)
	print(L) 
