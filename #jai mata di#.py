#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 



from collections import defaultdict
#start the code from here


n,k=map(int,input().split())

def dfs(a,b):
	for e in gr[a]:
		if e!=b:
			dfs(a,b)
			

l=[[0] for i in range(n)]
gr=defaultdict(list)
for i in range(n-1):
	a,b=map(int,input().split())
	a=a-1
	b=b-1
	gr[a].append(b)
	gr[b].append(a)
