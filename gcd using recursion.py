#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 


from math import *
#start the code from here
def hcf(a,b):
	if b!=0:
		return hcf(b,a%b)
	else:
		return b
t=int(input())
s=int(input())
e=gcd(t,s)
print(e)
def fact(a):
	if a==1 or a==0:
		return a
	else:
		return a*fact(a-1)
we=int(input())
print(fact(we))

def fibon(a):
	if a==0 or a==1:
		return a
	else:
		return(fibon(a-1)+fibon(a-2))
yu=int(input())
for i in range(yu):
	print(fibon(i),end=" ")
print()

class node():
	def __init__(self,data):
		self.data=data
		self.left=None
		self.right=None
bte=node(8)
btf=node(7)
btg=node(6)
btu=node(3)
root=btf
root.left=btg
root.left.left=btu
root.right=bte

def inorder(r):
	if r==None:
		return
	inorder(r.left)
	print(r.data)
	inorder(r.right)
inorder(root)

def postorder(r):
	if r==None:
		return
	postorder(r.left)
	postorder(r.right)
	print(r.data)
print("Post")
postorder(root)
def preorder(r):
	if r==None:
		return
	print(r.data)
	preorder(r.left)
	preorder(r.right)
print("preorder")
preorder(root)

def insertbst(root,item):
	if root.data>item:
		

