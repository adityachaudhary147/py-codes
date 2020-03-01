# 580A dp
#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 



def lisub(l,n):
	if n==1:
		return 1
	if n==2:
		if l[n-2]<=l[n-1]:
			return 2
		else:
			return 1
	else:
		return lisub(l,)

#start the code from here

t=int(input())
l=list(map(int,input().split()))
r=[1]*(len(l)-1)
m=1
for i in range(len(l)-1):
	if l[i+1]>=l[i]:
		if i==0:
			r[i]+=1
		else:
			r[i]=r[i-1]+1

		if r[i]>m:
			m=r[i]
# print(r)
print(m)
