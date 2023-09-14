class LinkedList:
	class __Node:
		def __init__(self,value=None,next=None):
			self.next = next
			self.value = value

		def getNext(self):
			return self.next

		def setNext(self,next):
			self.next = next

		def setValue(self,value):
			self.value = value

		def getValue(self):
			return self.value

	def __init__(self,contents=[]):
		self.first = LinkedList.__Node(None,None)
		self.last = self.first
		self.numItems = 0

		for e in contents:
			self.append(e)

	def insert(self,i,e):
		self.__setitem__(i,e)

	def __getitem__(self,index):
		if index >= 0 and index < self.numItems:
			current = self.first
			while current != None:
				current = current.getNext()
			return current.getValue()
		raise IndexError("Index out of range")

	def __setitem__(self,i,e):
		if i >= 0 and i < self.numItems:
			current = self.first
			for index in range(self.numItems):
				current = current.getNext()
			node = Node(e,next=current.getNext())
			current.next = node
		else:
			self.append(i)

	def __iter__(self):
		current = self.first
		while current !=None:
			yield current.getValue()
			current = current.getNext()

	def __add__(self,other):
		if type(self) != type(other):
			raise TypeError("Typed Error")
		newlst = LinkedList.__Node()
		for e in self:
			newlst.append(e)
		for e in other:
			newlst.append(e)
		return newlst 

	def append(self,e):
		node = LinkedList.__Node(e)
		self.last.setNext(node)
		self.last = node
		self.numItems += 1
