#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




#start the code from here

t=int(input())
for i in range(t):
	n=int(input())
	l=list(map(int,input().split()))
	su=sum(l)
	xo=0
	for j in range(n):
		xo^=l[j]
	# print(xo,"XOR")
	if 2*xo==su:
		print(0)
		print()
	else:
		print(2)
		print(xo,(su+xo))
	# print(xo,su)

