#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 

from collections import defaultdict

# simple DFS EDITED VERSION...... .. if visited again then output
def dfs(stack,visited,g):
	cc=0

	while stack:
		# print(stack,visited)
		p=stack.pop()
		if visited[p]!=2:
			visited[p]+=1
			cc+=1
			if visited[p]==2:
				# print(p+1,"pp")
				return cc-1
				# print("yes")
		for i in g[p]:
			# print(i,"kya dikkat h")
			if visited[i]!=2:
				stack.append(i)
		# print(stack)

def parent(par,a):
	if par[a]==a:
		return a
	else:
		return parent(par,par[a])
def union(par,a,b):
	c,d=parent(par,a),parent(par,b)
	if c==d:
		return
	else:
		# print("different")
		par[d]=c



t1=int(input())
for yu in range(t1):
	t=int(input())
	g=dict()
	l=list(map(int,input().split()))
	for i in range(t):
		l[i]-=1
	par=[i for i in range(t)]
	for i in range(t):
		union(par,i,l[i])
		# print(par)
	dicparent=dict()
	pset=set()
	rparent=dict()
	for i in range(t):
		f=parent(par,i)
		dicparent[i]=f
		pset.add(f)
	g=defaultdict(list)
	# print(par,"parentarray")
	# l=list(map(int,input().split()))
	for i in range(t):
		a,b=i+1,l[i]
		a=a-1
		b=b
		g[a].append(b)
	# print(g,"dictg")
	# print(pset,"parentset")
	for i in pset:
		visited=[0]*t
		stack=[i]
		rparent[i]=dfs(stack,visited,g)
		# print(i)
	# print(rparent)
	# print(dicparent)
	for i in range(t):
		print(rparent[dicparent[i]],end=' ')
	print()






