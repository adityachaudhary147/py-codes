#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




#start the code from here

t=int(input())
for i in range(t):
	e=int(input())
	l=list(map(int,input().split()))
	w=l.count(0)
	if w+sum(l)==0:
		print(w+1)
	else:
		print(w)

