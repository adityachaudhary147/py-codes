#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




#start the code from here
from collections import defaultdict
n,l=map(int,input().split())
graph=defaultdict(set)
for i in range(l):
	a,b=map(int,input().split())
	a=a-1
	b=b-1
	graph[a].add(b)
	graph[b].add(a)
ans=0
while True:
	rem=[]
	for i in graph:
		if len(graph[i])==1:
			rem.append(i)
	if len(rem)==0:
	 	break
	for i in rem:
		graph.pop(i)
		for e in graph:
			if i in graph[e]:
				graph[e].remove(i)
	ans+=1
print(ans)
