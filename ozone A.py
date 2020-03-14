#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




#start the code from here
t=int(input())
for i in range(t):
	st=input()
	l=list(map(int,input().split()))
	l2=list(map(int,input().split()))
	l.sort()
	l2.sort()
	print(*l)
	print(*l2)
