#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 


# def dfs(visited,stack,l,t):
# 	stack=[0]
# 	we=[]
# 	while(stack):
# 		p=stack.pop()
# 		if visited[p]==0:
# 			visited[p]=1
# 		for j in range(p+1,t):
# 			if l[j]-l[p]==j-p:
# 				stack.append(j)


def connected(v,w):
		# visit=[0]*v
		stack=[]
		ct=[]
		su=0
		for i in range(v):
			stack.append(i)
			l=[]
			sum1=0
			visit=[0]*v
			while stack:
				x=stack.pop()
				if visit[x]==0:
					if len(l)==0:
						l.append(x)
						visit[x]=1
						sum1+=w[x]

					else:
						if l[-1]-x==w[l[-1]]-w[x]:
							visit[x]=1
							sum1+=w[x]
							l.append(x)

				for j in range(x+1,t):
					if visit[j]==0:
						stack.append(j)
			if sum1>su:
				su=sum1
				# print(su,"changes")
		return su
#start the code from here
t=int(input())
l=list(map(int,input().split()))


print(connected(t,l))

