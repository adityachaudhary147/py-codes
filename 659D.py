#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




#start the code from here

t=int(input())
l=[]
e=0
r=t//2
r=r-2
for i in range(t):
	if len(l)==3:
		if l[0][0]==l[1][0] and l[2][0]>l[1][0]:
			e+=1
		elif l[0][1]==l[1][1] and l[2][1]>l[1][1]:
			e+=1
		l.pop(0)
	m,n=map(int,input().split())
	l.append((m,n))

print(r)		


