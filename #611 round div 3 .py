#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




#start the code from here
n,m=map(int,(input()).split())
l=list(map(int,input().split()))
lset2=set(l)
lset=set(l)
u=0
we=1
ans=0
while len(lset)<m+n:
	q=l[u]+we
	qw=l[u]-we
	if q not in lset:
		lset.add(q)
		ans+=we
	if len(lset)==m+n:
		break
	if qw not in lset:
		lset.add(qw)
		ans+=we
	we+=1
	u-=1
print(ans)
print(*(lset-lset2))

