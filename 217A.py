
#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 


# MADE BY ASTRIK WITH LOVE
#start the code from here
n=int(input())
global parent
parent=[i for i in range(n)]
# n is total number of nodes 
# finding parent of a node
def find(w):
	global parent
	if parent[w]==w:
			return w
	else:
		return find(parent[w])


def union(a,b):
	global parent
	w=find(a)
	y=find(b)
	if w==y:
		return 
	parent[y]=w


#start the code from here
l=[]
ans=0
for i in range(n):
	a,b=map(int,input().split())
	for u in range(len(l)):
		if l[u][0]==a or l[u][1]==b:
			union(u,i)
		else:
			ans+=1
	l.append([a,b])
pset=set()
for i in range(len(l)):
	pset.add(find(i))
print(len(pset)-1)


