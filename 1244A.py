#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




#start the code from here
from math import *
t=int(input())
for e in range(t):
	a,b,c,d,k=map(int,input().split())
	x=ceil(a/c)
	y=ceil(b/d)
	# print(x,y)
	if x+y<=k:
		print(x,y)
	else:
		print(-1)