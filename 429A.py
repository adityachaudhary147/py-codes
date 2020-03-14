#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




#start the code from here
t=int(input())
l=list(map(int,input().split()))
se=set()
ans=0
for i in range(len(l)):
	sdf=len(se)
	se.add(l[i])
	nlen=len(se)
	if nlen==sdf:
		se.remove(l[i])
	ans=max(ans,len(se))
print(ans)

