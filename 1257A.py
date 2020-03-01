#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




#start the code from here

t=int(input())
for i in range(t):
	n,x,a,b=map(int,input().split())
	w=abs(b-a)
	if n-1==w:
		print(w)
	elif n-1>=w+x:
		print(w+x)
	else:
		print(n-1)

