#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 

import math
def dfscon(gr,cost,n):
	visited=[0]*n
	ans=0
	for i in range(n):
		stack=[i]
		co=math.inf
		while stack:
			p=stack.pop()
			if visited[p]==0:
				if cost[p]<co:
					co=cost[p]
				visited[p]=1
			for yu in gr[p]:
				if visited[yu]==0:
					stack.append(yu)
		if co!=math.inf:
			ans=ans+co
	return ans






from collections import defaultdict
#start the code from here
n,t=map(int,input().split())
l=list(map(int,input().split()))
gr=defaultdict(list)
for u in range(t):
	a,b=map(int,input().split())
	a=a-1
	b=b-1
	gr[a].append(b)
	gr[b].append(a)
# print(gr)
ans=dfscon(gr,l,n)
print(ans)


