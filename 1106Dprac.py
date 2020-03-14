#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 



from collections import defaultdict
from queue import PriorityQueue

#start the code from here
a,b=map(int,input().split())
graph=defaultdict(list)
for i in range(b):
	n,m=map(int,input().split())
	graph[n-1].append(m-1)
	graph[m-1].append(n-1)
q= PriorityQueue()
q.put(0)
ans=[]
visited=[0]*a
while not q.empty():
	p=q.get()
	if visited[p]==0:
		ans.append(p+1)
		# print(p+1)
		visited[p]=1
	for i in graph[p]:
		if visited[i]==0:
			q.put(i)
print(*ans)



