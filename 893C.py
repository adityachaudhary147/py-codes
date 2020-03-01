#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 


t,n=map(int,(input().split()))
global parent
global cost
cost=list(map(int,input().split()))
parent=[i for i in range(t)]

def find(w):
	global parent
	if parent[w]==w:
			return w
	else:
		a=find(parent[w])
		return a


def union(a,b):
	global parent
	w=find(a)
	y=find(b)
	if w==y:
		return
	if cost[w]<cost[y]:
		parent[y]=w
	else:
		parent[w]=y
for i in range(n):
	a,b=map(int,input().split())
	union(a-1,b-1)
	# print(parent,a-1,b-1)
ans=0
pset=set()

if t==n+1:
	print(min(cost))
	exit()
for i in range(t):
	try:
		pset.add(find(i))
	except:
		continue
# print(pset)
for u in pset:
	ans+=cost[u]
print(ans)

