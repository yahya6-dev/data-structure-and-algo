class List:
	def __init__(self,contents=[],size=10):
		self.items =  [None] * size		#this run O(1) if empty else it runs O(n)
		self.size = size
		self.numItems = 0
		for e in contents:
			self.append(e)

	#make more room other element to have O(1) append using amortized analysis
	def _makeroom(self):
		newsize = (self.size//4) + self.size + 1
		newlst = [None] * newsize
		for i in range(self.numItems):
			newlst[i] = self.items[i]

		self.size = newsize
		self.items = newlst

	def append(self,e):
		#it runs O(1)
		if self.numItems == self.size:
			self._makeroom()

		self.items[self.numItems] = e
		self.numItems += 1

	def __iter__(self):
		#this run O(n)
		for i in range(self.numItems):
			yield self.items[i]

	def __contains__(self,x):
		#this run O(n)
		for i in range(self.numItems):
			if self.items[i] == x:
				return True
		return False
	def __add__(self,other):
		newlst = List(size=other.numItems+self.numItems)
		for e in other:
			newlst.append(e)
		for e in self:
			newlst.append(e)

		return newlst

	def __len__(self):
		return self.numItems

	def __getitem__(self,index):
		if index >= 0 and index < self.numItems:
			return self.items[index]
		raise IndexError("Crossing Bound Exception")

	def __setitem__(self,i,e):
		if i >= 0 and i < self.numItems:
			self.items[i] = e
		raise IndexError("Crossing Bound Exception")

	def __eq__(self,other):
		#run O(n)
		if type(self) != type(other):
			return False
		if len(other) != len(self):
			return False
		for i in range(self.numItems):
			if self[i] != other[i]:
				return False
		return True

	def insert(self,i,e):
		if i < self.numItems:
			for j in range(i-1,self.numItems,-1):
				self.items[j+1] = self.items[j]
			self.items[i] = e
		else:
			self.append(e)

	def __delitem__(self,i):
		for index in range(i,self.numItems-1):
			self.items[index] = self.items[index+1]
		self.numItems -= 1

	def __str__(self):
		s = "["
		for i in range(self.numItems):
			s = s + repr(self.items[i])
			if i < self.numItems-1:
				s = s+","
		s = s+"]"
		return s

	def __repr__(self):
		s = "["
		for i in range(self.numItems):
			s = s + repr(self.items[i])
			if i < self.numItems-1:
				s = s+","
		s = s+"]"
		return s