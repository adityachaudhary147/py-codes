#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 

class graph():
	"""docstring for grpaph"""
	def __init__(self,nver):
		self.adlist=defaultdict(list)
		self.n=nver
	# startingwith a node number i
	def insertvertex(self,a,b):
		self.adlist[a].append(b)
		self.adlist[b].append(a)

	def dfs(self,i):
		self.visited=[0]*self.nver
		self.stack=[i]
		while self.stack:
			p=self.stack.pop()
			if visited[p]==0:
				# visit p
				print(p)
			for u in self.adlist[p]:
				if visited[u]==0:
					self.stack.append(u)
		

from collections import defaultdict
#start the code from here
t=int(input())

# graph=defaultdict(list)
newg=graph(t)
for e in range(t):
	a,b=map(int,input().split())
	graph.insertvertex(a,b)
graph.dfs(0)
