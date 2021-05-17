#jai mata di#
import sys
# sys.stdin = open('input.in', 'r')  
# sys.stdout = open('output.out', 'w') 


# no of vertices
# n=int(input())
n=5
# g=[[0 for i in range(n) ] for j in range(n)]
# adjacency matrix sample 
gra=[[0, 2, 0, 6, 0],[2, 0, 3, 8, 5],[0, 3, 0, 0, 7],[6, 8, 0, 0, 9],[0, 5, 7, 9, 0]]
# prims for MST minimum spanning tree
# in this vertices are added to mst
# first add 0th vertx as visited
statusvertex=[False for i in range(n)]
# statusvertex[0]=True
currentweight=[float('inf') for i in range(n)]
currentweightcp=list(currentweight)
# assume for zero vertex
currentweight[0]=0
startindex=0
parent=[None for i in range(n)]
parent[0]=-1
for j in range(n):
	startindex=currentweight.index(min(currentweight))
	# print(startindex)
	statusvertex[startindex]=True
	for v in range(n):
		if gra[startindex][v]>0 and statusvertex[v]==False and currentweightcp[v]>gra[startindex][v]:
			parent[v]=startindex
			currentweight[v]=gra[startindex][v]
			currentweightcp[v]=gra[startindex][v]
			currentweight[startindex]=float('inf')
	# print(parent)
	# print(statusvertex)
print("MST is ")
# print(parent)
for i in range(1,n):
	print(parent[i],"--",i,gra[i][parent[i]])





