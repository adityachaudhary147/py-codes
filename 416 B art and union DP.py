#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




#start the code from here
n,m=map(int,input().split())
main=[[] for i in range(m)]
for w in range(n):
	li=list(map(int,input().split()))
	for i in range(len(li)):
		main[i].append(li[i])
w=main[0]
ans=[0 for i in range(n)]
ans[0]=w[0]
for i in range(1,n):
	ans[i]=ans[i-1]+w[i]
for u in range(1,m):
	r=main[u]
	ans[0]=ans[0]+r[0]
	for w in range(1,n):
		if ans[w-1]>ans[w]:
			ans[w]=ans[w-1]+r[w]
		else:
			ans[w]=ans[w]+r[w]
print(*ans)