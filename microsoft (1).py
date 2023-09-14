from collections import Counter
import math

def find(L):
	items = Counter(L)
	items = sorted(list(items.items()), key = lambda x: x[1] )
	maximum = items[-1]
	expression = math.floor(len(L) / 2.0)
	if (maximum[1] >  expression):
	 return maximum[0]
	return


print(find([1, 2, 1, 1, 3,2,2,2,2,2]))
