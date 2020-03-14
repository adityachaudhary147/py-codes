# jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 

def find(parent,a):
	if parent[a]==a:
		return a
	else:
		parent[a]=find(parent,parent[a])
		return parent[a]
def union(parent,rank,a,b):
	a=find(parent,a)
	b=find(parent,b)
	if a==b:
		return
	rank[a]+=rank[b]
	parent[b]=parent[a]
	return
n,m=map(int,input().split())
parent=[i for i in range(n)]
rank=[1 for i in range(n)]
for i in range(m):
	l=list(map(int,input().split()))
	we=l.pop(0)
	for j in range(1,we):
		union(parent,rank,l[0]-1,l[j]-1)

for i in range(n):
	print(rank[find(parent,i)],end=" ")

