#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 



# MADE BY ASTRIK WITH LOVE
#start the code from here
n=int(input())
global parent
parent=[i for i in range(27)]
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
present=[0]*26

for u in range(n):
	st=input()
	parent[ord(st[0])-ord('a')]=ord(st[0])-ord('a')
	for i in range(len(st)):
		union(ord(st[0])-ord('a'),ord(st[i])-ord('a'))
		present[ord(st[i])-ord('a')]+=1
se=set()
for i in range(26):
	if (present[i]>0):
		pa=find(i)
		se.add(pa)
print(len(se))






