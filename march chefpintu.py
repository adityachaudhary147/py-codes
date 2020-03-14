# #jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 


#start the code from here
t=int(input())

for i in range(t):
	a,b=map(int,input().split())
	l=list(map(int,input().split()))
	p1=list(map(int,input().split()))
	newl=[0]*(b+1)
	se=set()
	for k in range(len(l)):
		newl[l[k]]=p1[k]+newl[l[k]]
		se.add(l[k])
	amin=1000000
	# print(newl)
	for j in se:
		amin=min(newl[j],amin)
	print(amin)