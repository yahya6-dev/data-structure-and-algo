def returndict(s1):
	i = 0
	d1 = {}
	for i in range(len(s1)):
		if s1[i] in d1:
			d1[s1[i]] += 1
		else:
			d1[s1[i]] = 1
	return d1

def compare(s1,s2):
	d1 = returndict(s1)
	d2 = returndict(s2)
	result = sum(d1.values()) - sum(d2.values())
	if result < 0:
		return -1
	elif result > 0:
		return 1
	elif result == 0:
		return 0

