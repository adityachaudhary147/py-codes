#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




from collections import defaultdict
#start the code from here
# no of egdes..


# simple DFS EDITED VERSION......
def dfs(stack,visited,g,er):

	while stack:
		# print(stack,visited)
		p=stack.pop()
		if visited[p]==0:
			visited[p]+=1
			er.append(p+1)
				# print("yes")
		for i in g[p]:
			# print(i,"kya dikkat h",g[p])
			# print(visited,stack)
			if visited[i]==0:
				stack.append(i)
		# print(visited,stack,"final")
		# print(stack)


g=defaultdict(list)


#start the code from here
e,fin=map(int,input().split())
l=list(map(int,input().split()))
for i in range(e-1):
	a,b=i,l[i]+i
	a=a
	b=b
	g[a].append(b)
# print(g)
visited=[0]*e
stack=[0]
er=[]
dfs(stack,visited,g,er)
# print(er)
if visited[fin-1]==1:
	print("YES")
else:
	print("NO")

