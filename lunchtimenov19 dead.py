#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




#start the code from here

t=int(input())
for i in range(t):
	e=int(input())
	l=list(map(int,input().split()))
	l.sort()
	cc=0

	q=[]
	cc1=0
	a=l[0]