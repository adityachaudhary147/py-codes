#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




#start the code from here

t=int(input())
for i in range(t):
	n,s=map(int,input().split())
	l=list(map(int,input().split()))
	cc=0
	qq=l[0]
	iqq=0
	h=0
	for j in range(n):
		cc=cc+l[j]
		if qq<l[j]:
			qq=l[j]
			iqq=j
		if cc>s:
			h=1
			break
	if h==0:
		print(0)
	else:
		print(iqq+1)	



