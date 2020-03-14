#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




#start the code from here
t=int(input())
for i in range(t):
	a,b=map(int,input().split())
	if pow(a,1,b)==0:
		print("YES")
	else:
		print("NO")

