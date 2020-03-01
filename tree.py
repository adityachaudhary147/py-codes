#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




#start the code from here



class bst:
	class _node():
		def __init__(self,val,left=None,right=None):
			self.val = val
			self.left=left
			self.right=right
		def getvalue(self):
			return self.value
		def setvalue(self,nval):
			self.value=nval
		def getleft(self):
			return self.value
		def setleft(self,nleft):
			self.felt=nleft
		def getright(self):
			return self.right
		def setright(self,nright):
			self.right=nright
		def 
	def __init__(self):
		self.root=None
	def insert(self,value):
		def __insert(root,value):
			if root==None:
				return bst._node(value)
			if val<root.getvalue():
				return root.setleft(__insert(root.getleft(),value))
			else:
				return root.setright(__insert(root.getright(),value))
			return root
		self.root = __insert(self.root,value)
	def __iter__(self):
		if self.root != None:
			return self.root.__iter__()
		else:
			return [].__iter__()





		
			
