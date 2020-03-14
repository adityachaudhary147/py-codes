#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 



from collections import defaultdict
def dfscon(gr,n,ans):
	for i in range(n):
		day=0
		stack=[i]
		while stack:
			visited=[0]*n
			p=stack.pop()
			day+=1
			if visited[p]<2:
				visited[p]+=1
				if visited[p]==2:
					ans[p]=int(day)
					break

			for yu in gr[p]:
				if visited[yu]<2:
					stack.append(yu)
#start the code from here
t=int(input())
for i in range(t):
	gr=defaultdict(list)
	n=int(input())
	l=list(map(int,input().split()))
	for j in range(len(l)):
		gr[j].append(l[j]-1)
	# print(gr)
	ans=[0]*n
	dfscon(gr,n,ans)
	print(ans)


