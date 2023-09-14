class List:
	#this run O(n) for non empty else O(1) 
	def __init__(self,contents=[],size=10):
		self.items = [None]*size
		self.size = size
		self.numItems = 0


	def append(self,e):
		#this run O(1) amortized complexity
		if self.numItems == self.size:
			self._makeroom()

		self.items[self.numItems] = e
		self.numItems += 1

	def _makeroom(self):
		newsize = (self.size//4) + self.size+1
		nlst = [None]*newsize
		for i in range(len(self.numItems)):
			nlst[i] = self.items[i]

		self.size = newsize
		self.items = nlst

	#O(1) complexity
	def __len__(self):
		return self.numItems

	def __eq__(self,other):
		#run O(n) complexity
		if type(other) != type(self):
			return False
		if len(other) != len(self):
			return False
		for i in range(self.numItems):
			if other[i] != self[i]:
				return False
		return True

	#run O(n) Complexity
	def __contains__(self,e):
		for item in self.items:
			if item == e:
				return True
		return False

	#run O(1)
	def __getitem__(self,index):
		if index >= 0 and index < self.numItems:
			return self.items[index]
		raise IndexError("OutOfBound Exception")

	#run O(1)
	def __setitem__(self,i,e):
		if i >= 0 and i < self.numItems:
			self.items[i] = e
		raise IndexError("OutOfBound Exception")

	#run O(n)
	def insert(self,i,e):
		if i < self.numItems-1:
			for j in range(i-1,self.numItems-1,-1):
				self.items[j+1] = self.items[j]
			self.items[i] = e
		else:
			self.append(e)

	#run O(n)
	def __delitem__(self,i):
		for j in range(i,self.numItems-1):
			self.items[j] = self.items[j+1]
		self.numItems -= 1

	def __iter__(self):
		for i in range(self.numItems):
			yield self.items[i]
	#run O(n)
	def __add__(self,other):
		nlst = List(size=other.numItems+self.numItems)
		for e in other:
			nlst.append(e)
		for e in self:
			nlst.append(e)
		return nlst
	#run O(n)
	def __str__(self):
		s = "["
		for i in range(self.numItems):
			s = s + repr(self.items[i])
			if  i < self.numItems-1:
				s = s+","
		s = s+"]"
		return s


if __name__=="__main__":
	l = List()
	for i in range(10):
		l.append(i)
	print(l)
	l.insert(2,"Nothing")
	print(l)
	del l[2]
	print(l)
	print(l[2])
	print(l+l)