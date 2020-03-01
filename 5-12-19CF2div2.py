#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




#start the code from here

t=int(input())
for i in range(t):
	r=int(input())
	l=list(map(int,input().split()))
	l2=[i for i in range(1,r+1)]
	for i in range(r):
		a=l[i]
		l2[a-1]=i+1
	ans=[1]
	p=0
	q=0
	ma=l2[0]
	mi=l2[0]
	for j in range(1,r):
		if l2[j]>ma:
			ma=l2[j]
		if l2[j]<mi:
			mi=l2[j]
		u=ma-mi
		if u==j:
			ans.append(1)
		else:
			ans.append(0)
	print(*ans,sep="")

