class MyList:
	def __init__(self,contents = [], size=10):
		self.items = [None]*size
		self.numItems = 0
		self.size = size
		for e in contents:
			self.append(e)

	def append(self,x):
		if self.numItems == self.size:
			self._makeroom()
		self.items[self.numItems] = x
		self.numItems += 1

	def _makeroom(self):
		newsize = (self.size//4) + self.size + 1
		newlst = [None] * newsize
		
		for i in range(self.numItems):
			newlst[i] = self.items[i]

		self.items = newlst
		self.size = newsize

	def __getitem__(self,index):
		if index >= 0 and index < self.numItems:
			return self.items[index]

		raise IndexError("Out Of Bound Exception")

	def __setitem__(self,index,item):
		if index >= 0 and index < self.numItems:
			self.items[index] = item
		raise IndexError("Out Of Bound Exception")

	def __iter__(self):
		for i in range(self.numItems):
			yield self.items[i]

	def __len__(self):
		return self.numItems

	def __contains__(self,x):
		for item in self:
			if item == x:
				return True
		return False

	def __str__(self):
		s = "["
		for i in range(self.numItems):
			s = s + repr(self.items[i])
			if i < self.numItems-1:
				s = s + ","
		s = s+"]"
		return s

	def __repr__(self):
		s = "["
		for i in range(self.numItems):
			s = s + repr(self.items[i])
			if i < self.numItems-1:
				s = s + ","
		s = s+"]"
		return s

	def __add__(self,other):
		newlst = MyList(size=self.numItems+other.numItems)
		for e in other:
			newlst.append(e)
		for e in self:
			newlst.append(e)

		return newlst

	def __eq__(self,other):
		if type(self) != type(other):
			return False
		if len(self) != len(other):
			return False

		for i in range(self.numItems):
			if self[i] != other[i]:
				return False
		return True

	def insert(self,i,e):
		if i < self.numItems:
			for j  in range(self.numItems-1,i-1,-1):
				self.items[j+1] = self.items[j]
			self.items[i] = e
		else:
			self.append(e)

	def __delitem__(self,i):
		for j in range(i,self.numItems-1):
			self.items[j] = self.items[j+1]
		#self.items[j+1] = None
		self.numItems -= 1

