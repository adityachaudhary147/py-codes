#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




#start the code from here


#start the code from here
 
s=input()
l=list(map(int,s))
r=1
ans=0
k=0

l1=list(l)
for op in range(1,len(s)):
	l1[op]=l1[op-1]+l1[op]
# print(l1)
while r!=len(l)+1:
	# qs=sum(l[k:k+r])
	if k==k+r-1:
		qs=l[k]
	elif k==0:	
		qs=l1[r-1]
	else:
		qs=l1[k+r-1]-l1[k-1]
	
	# print(k,k+r)
	# print(qs)
	if qs>0:
		if r%qs==0:
			ans+=1
	k=k+1
	if k+r==len(l)+1:
		k=0
		r=r+1
 
print(ans)