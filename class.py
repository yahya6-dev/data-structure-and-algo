class LinkedList:
	class __Node:
		def __init__(self,value=None,next=None):
			self.value = value
			self.next = next

		def setNext(self,next):
			self.next = next

		def setValue(self,value):
			self.value = value

		def getValue(self):
			return self.value

		def getNext(self):
			return self.next

	def __init__(self,contents=[]):
		self.numItems = 0
		self.first = LinkedList.__Node(None,None)
		self.last = self.first

		for e in contents:
			self.append(e)

	def append(self,e):
		node = LinkedList.__Node(e)
		self.last.setNext(node)
		self.last = node
		self.numItems += 1 

	def __iter__(self):
		current = self.first
		while current != None:
			yield current.getValue()
			current = current.getNext()

	def remove(self,index):
		current = self.first
		for i in range(index):
			current = current.getNext()
		current.next = current.getNext()
		self.first = current

if __name__=="__main__":
	l = LinkedList()
	for e in range(10):
		l.append(e)
	for e in l: print(e)
	l.remove(3)
	for e in l:print(e)