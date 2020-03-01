#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




#start the code from here
t=int(input())
for i in range(t):
	a,b=map(int,input().split())
	if a-b==1:
		print("NO")
	else:
		print("YES")


