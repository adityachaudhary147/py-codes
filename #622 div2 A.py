#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




#start the code from here

t=int(input())
l=list(map(int,input().split()))
e=[0]*(t-1)
for i in range(1,len(l)):
	if l[i-1]<=l[i]:
		e[i-1]=0
	else:
		e[i-1]=1
print()

	
	

