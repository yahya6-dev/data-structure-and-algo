class LinkedList:
	class __Node:
		def __init__(self,value,next=None):
			self.value = value
			self.next = next

		def getNext(self):
			return self.next

		def setNext(self,next):
			self.next = next
		def setValue(self,value):
			self.value = value
		def getValue(self):
			return self.value
		def __str__(self):
			return repr((self.value,self.next)) 

	def __init__(self,next=None):
		self.first = LinkedList.__Node(None,None)
		self.last = self.first
		self.numItems = 0
		if next:
			self.append(next)

	def __iter__(self):
		current = self.first.getNext()
		while current != None:
			yield current.getValue()
			current = current.getNext()

	def append(self,e):
		node = LinkedList.__Node(value=e)
		self.last.setNext(node)
		self.last =  node
		self.numItems += 1 

	def insert(self,i,e):
		if i < self.numItems:
			current = self.first
			for index in range(i):
				current = current.getNext()
			node = LinkedList.__Node(e,current.getNext())
			current.setNext(node)
			self.numItems +=1
		else:
			self.append(e)



	def __getitem__(self,index):
		if index >= 0 and index < self.numItems:
			current = self.first.getNext()
			for i in range(index):
				current = current.getNext()
			return current.getValue()

		raise IndexError("Index out of range!")


	def __setitem__(self,i,e):
		if i <= 0 and i < self.numItems:
			current = self.first.getNext()
			for i in range(i):
				current = current.getNext()
			node = LinkedList.__Node(e,current.getNext())
			current.setNext(node)
		raise IndexError("Index out of range!")

	def __len__(self):
		return self.numItems

	def __add__(self,other):
		newlst = LinkedList()
		current = other.first.getNext()
		while current != None:
			newlst.append(current.getValue())
			current = current.getNext()
		current = self.first.getNext()
		while current != None:
			newlst.append(current.getValue())
			current = current.getNext()
		return newlst

	def __str__(self):
		return str(self.first)

if __name__=="__main__":
	n = LinkedList()
	for e in range(10):
		n.append(e)
	print(n)
	n.insert(2,"Hornet")
	print(n[2],"here")
	for e in n:
		print(e)
	for e in (n+n): print(e)
