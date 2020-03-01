#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 



from collections import defaultdict
#start the code from here
# no of egdes..
t=int(input())

g=defaultdict(list)
l=list(map(int,input().split()))
c=list(map(int,input().split()))
for i in range(t-1):
	a,b=i+2,l[i]
	a=a-1
	b=b-1
	g[b].append(a)
copyc=[0]*t
# print(g)
ans=0
visited=[0]*t
stack=[0]
# simple DFS EDITED VERSION......
while stack:
	# print(stack)
	p=stack.pop()
	if visited[p]==0:
		visited[p]=1
		if copyc[p]!=c[p]:
			ans+=1
			# print("yes")
	for i in range(len(g[p])):
		if visited[g[p][i]]==0:
			stack.append(g[p][i])
			copyc[g[p][i]]=c[p]
	# print(stack)
print(ans)



