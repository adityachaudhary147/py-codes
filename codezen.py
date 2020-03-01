#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




#start the code from here

t=int(input())
for i in range(t):
	n=int(input())
	l=[0]*400
	l[0]=0
	l[1]=1
	l[2]=2
	l[3]=3
	for r in range(4,40):
		l[r]=l[r-1]+l[r-2]+l[r-3]+1
	print(l[n])