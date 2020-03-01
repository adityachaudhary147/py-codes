#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




#start the code from here
n,m,b=map(int,input().split())
b=b%n
if b+m>=0:
	e=abs(m+b)%n
else:
	e=abs(n+b+m)%n

if e==0:
	print(n)
else:
	print(e)