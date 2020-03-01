#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




#start the code from here

t=int(input())
for i in range(t):
	w=int(input())
	l=[0,0 for i ]
	j=0
	for k in range(int(w)):
		a,b=list(map(int,input().split()))
		l[j]=a
		j=j+1
		l[j]=b
		j=j+1
	print(l)
