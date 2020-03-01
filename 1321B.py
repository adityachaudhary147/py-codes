#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 



from collections import Counter
#start the code from here
t=int(input())
l=list(map(int,input().split()))
l1=[0]*t
ans=0
dic=dict()
ans=0
for i in range(t):
	l1[i]=l[i]
	ty=l[i]-i
	# print(ty)
	if ty in dic:
		dic[ty]+=l[i]
	else:
		dic[ty]=l[i]
	ans=max(dic[ty],ans)
print(ans)