#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




#start the code from here
A=int(input())
l1=[[0 for i in range(A)] for i in range(A)]
a1=0
b1=A
c1=0
d1=A
r=0
while True:
	for i in range(a1,b1):
		r+=1
		l[c1][i]=r
	c1+=1
	for i in range(c1,d1):
		r+=1
		l[i][d1-1]=r
	d1-=1
	for i in range(a1,b1):
		r+=1
		l[c1][i]=r
	a1+=1
	for i in range(c1,d1):
		r+=1
		l[i][b1-1]=r
	b1-=1
