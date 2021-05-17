#jai mata di#
import sys
# sys.stdin = open('input.in', 'r')  
# sys.stdout = open('output.out', 'w') 
# creted by aditya chaudhary
# from collections import defaultdict
#start the code from here
# n=int(input())
# vertices
n=5
global parent
global rank
parent=[i for i in range(5)]
rank=[0 for i in range(5)]
# n is total number of nodes 
# finding parent of a node
def find(w):
	global parent
	if parent[w]==w:
			return w
	else:
		parent[w]=find(parent[w])
		return parent[w]


def union(a,b):
	global parent
	global rank
	w=find(a)
	y=find(b)
	if w==y:
		return
	if rank[w]>rank[y]:
		parent[y]=w
	elif rank[y]>rank[w]:
		parent[w]=y
	else:
		parent[w]=y
		rank[w]+=1

global gr
gr=list()


def addEdge(u,v,wt):
	global gr
	l=[u,v,wt]
	gr.append(l)

# u v and weight 
addEdge(0, 1, 10) 
addEdge(0, 2, 6)
addEdge(0, 3, 5) 
addEdge(1, 3, 15) 
addEdge(2, 3, 4)

gr.sort(key=lambda x:x[2]) 
# print(gr)
statusvertex=[False for i in range(n)]
ans=[]
for w in range(5):
	c=gr[w]
	u,v,wt=c[0],c[1],c[2]
	pu=find(u)
	pv=find(v)
	if pu==pv:
		nothing=0
	else:
		ans.append(c)
		union(u,v)

print(*ans)


