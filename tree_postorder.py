class PlusNode:
	def __init__(self,left,right):
		self.left,self.right = left,right

	def eval(self):
		return self.left.eval() + self.right.eval()
	def postorder(self):
		return "%s %s +" %(self.left.postorder(),self.right.postorder())


class NumNode:
	def __init__(self,value):
		self.value = value
	def eval(self):
		return self.value
	def postorder(self):
		return repr(self.value)

class TimeNode:
	def __init__(self,left,right):
		self.left,self.right = left,right
	def eval(self):
		return self.left.eval()*self.right.eval()
	def postorder(self):
		return "%s %s *"%(self.left.postorder(),self.right.postorder())

if __name__=="__main__":
	x,y = NumNode(20),NumNode(20)
	p =  PlusNode(x,y)
	t = TimeNode(p,NumNode(2))
	print(t.postorder())
