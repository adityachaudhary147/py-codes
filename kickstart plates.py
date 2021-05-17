#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




#start the code from here
t=int(input())
for i in range(t):
	n,p,k=map(int,input().split())
	precal=[0 for i in range(p)]
	# n is no of stacks
	# p is no of element in each stack
	# if k is samller than p than ans==precal value
	for e in range(n):
		l=list(map(int,input().split()))
		for h in range(1,p):
			l[h]=l[h-1]+l[h]
		for u in range(p):
			precal[u]=max(precal[u],l[u])

