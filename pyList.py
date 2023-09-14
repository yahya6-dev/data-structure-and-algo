class PyList:
	def __init__(self,size=1):
		self.items = [None]*size
		self.numItems = 0

	def append(self,item):
		if self.numItems == len(self.items):
			newLst = [None] * self.numItems * 2
			for i in range(len(self.items)):
				newLst[i] = self.items[i]
			self.items = newLst
			print(self.items)
		self.items[self.numItems] = item
		self.numItems += 1 
	def __iter__(self):
		for item in self.items:
			yield item

if __name__=="__main__":
	myList = PyList(3)
	for i in range(10000):
		myList.append(i)
	for x in myList:
		print(x,end=' ') 
