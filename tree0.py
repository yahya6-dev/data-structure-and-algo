class PlusNode:
	def __init__(self,left,right):
		self.left,self.right = left,right

	def eval(self):
		return self.left.eval() + self.right.eval()

	def inorder(self):
		return "(%s + %s)" %(self.left.inorder(),self.right.inorder())

class NumNode:
	def __init__(self,value):
		self.value = value

	def eval(self):
		return self.value

	def inorder(self):
		return "%s"%self.value

class TimeNode:
	def __init__(self,left,right):
		self.left,self.right = left,right
	def eval(self):
		return self.left.eval()*self.right.eval()

	def inorder(self):
		return "(%s * %s)" %(self.left.inorder(),self.right.inorder())

if __name__=="__main__":
	x,y =  NumNode(20),NumNode(20)
	p = PlusNode(x,y)
	m = TimeNode(p,NumNode(2))
	print(m.inorder())

