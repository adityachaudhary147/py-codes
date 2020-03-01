#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




#start the code from here

t=int(input())
for i in range(t):
	l=list(map(int,input().split()))
	l.sort()
	h=0

	if l[-1]-l[1]-1<=l[0] and l[0]<=l[-1]+l[1]+1:
		print("Yes")
	else:
		print("No")

