#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 

def dfsconnring(graph,n):
	
	count=0
	main=[]
	cc=0
	visited=[0]*n
	for i in range(n):
		if visited[i]==0 and len(graph[i])==2:
			stack=[i]
		else:
			continue
		h=0
		l=[]
		while stack:
			# print(stack)
			p=stack.pop()
			if visited[p]==0:
				visited[p]+=1
				# print("visited",p)
				l.append(p)
			if len(graph[p])!=2:
				h=1
			for yu in graph[p]:
				if visited[yu]==0:
					stack.append(yu)
			# print(stack)
		if h==0 and len(l)>0:
			# print(l)
			cc+=1
	return cc




from collections import defaultdict
#start the code from here
n,m=map(int,input().split())
graph=defaultdict(list)
for i in range(m):
	a,b=map(int,input().split())
	a=a-1
	b=b-1
	graph[a].append(b)
	graph[b].append(a)
# print(graph)
print(dfsconnring(graph,n))




