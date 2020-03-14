#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




#start the code from here
t=int(input())
# st=input()
for i in range(t):
	a,b=map(int,input().split())
	l=list(map(int,input().split()))
	print(min(b,sum(l)))

