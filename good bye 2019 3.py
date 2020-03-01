#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




#start the code from here

s=input()
l=list(map(int,s))
r=1
ans=0
k=0
su=[[0]*(len(s)+1)]*(len(s)+1)
# print(su)
l1=list(l)
for k in range(1,len(s)):
	l1[k]=l1[k-1]+l1[k]
print(l1)
cc=0
while r!=len(l)+1:
	cc+=1
	if k==k+r-1:
		qs=l[k]
	elif k==0:
		qs=l1[r-1]
	else:
		qs=l1[k+r-1]-l1[k]
	print(qs)
	if qs>0:
		if r%qs==0:
			ans+=1
	k=k+1
	if k+r==len(l)+1:
		k=0
		r=r+1

print(ans)


print(cc)