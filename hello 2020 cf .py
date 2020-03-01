#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




#start the code from here

n,m=map(int,input().split())
l=list(map(str,input().split()))
l1=list(map(str,input().split()))
t=int(input())
for i in range(t):
	e=int(input())
	print(l[e%n-1],end='')
	print(l1[e%m-1])

