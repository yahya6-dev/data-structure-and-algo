class PlusNode:
	def __init__(self,left,right):
		self.left = left
		self.right = right
	def eval(self):
		return self.left.eval()+self.right.eval()

	def preorder(self):
		return "+ %s %s"%(self.left.preorder(),self.right.preorder())


class NumNode:
	def __init__(self,value):
		self.value = value
	def preorder(self):
		return repr(self.value)
	def eval(self):
		return self.value

class TimeNode:
	def __init__(self,left,right):
		self.left = left
		self.right = right


	def eval(self):
		return self.left.eval()*self.right.eval()

	def preorder(self):
		return "* %s %s"%(self.left.preorder(),self.right.preorder())

if __name__=="__main__":
	x,y = NumNode(20),NumNode(20)
	p = PlusNode(x,y)
	t = TimeNode(p,NumNode(2))
	print(t.preorder())
