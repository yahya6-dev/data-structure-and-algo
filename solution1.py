# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.8.10
	if len(A) == 0: return
	A = sorted(list(set(A)))
	for i in range(len(A)):
		try:
			f = A[i]+1
			s = A[i+1]
			if f > 0 and f != s:
				return f
			elif f < 0 and f !=s: return 1
		except:
			s = A[-1]
			if s > 0:
				return s+1
			else: return 1
                 
