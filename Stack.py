class Stack:
	def __init__(self,contents=[]):
		self.stack = []
		for e in contents:
			stack.push(e)


	def isEmpty(self):
		return len(self.stack) == 0

	def push(self,e):
		self.stack.append(e)

	def pop(self):
		if self.isEmpty():
			raise RuntimeError("Stack is empty can not get item")
		top = self.stack[len(stack)-1]
		del self.stack[len(self.stack)-1] 
		return top

	def top(self):
		if self.isEmpty():
			raise RuntimeError("Stack is empty")
		return self.stack[len(self.stack)-1]

	def __iter__(self):
		for i in range(len(self.stack)-1,-1,-1):
			yield self.stack[i]

if __name__=="__main__":
	s = Stack()
	print("creation")
	for e in range(200):
		s.push(e)
	for e in s:
		print(e)