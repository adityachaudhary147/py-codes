#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




#start the code from here

t=int(input())
for i in range(t):
	e=int(input())
	l=[0,0,0,0,0,0,0,0,0]
	for j in range(e):
		w,r=(map(int,input().split()))
		if w<9:
			if l[w]<r:
				l[w]=r
	print(sum(l))