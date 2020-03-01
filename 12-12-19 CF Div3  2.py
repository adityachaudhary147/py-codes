#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 


def calc(x):
	if x<0:
		return 0
	else:
		return (x*(x+1))//2

#start the code from here

n,k=map(int,input().split())
s=input()
e=list(map(str,input().split()))
l=[-1]
ans=0
for i in range(len(s)):
	if s[i] not in e:
		l.append(i)
		if len(l)>1:
			q=l[-1]-l[-2]-1
			ans+=calc(q)
if l[-1]!=len(s)-1:
	q=len(s)-1-l[-1]
	ans+=calc(q)
print(ans)


