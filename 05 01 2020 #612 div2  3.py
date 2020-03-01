#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




#start the code from here

t=int(input())
l=list(map(int,input().split()))
s=set(l)
w={i for i in range(1,t+1)}
r=w-s
print(r)
for i in range(t):
	q=l[i]%2
	l[i]=q
print(l)