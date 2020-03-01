#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




#start the code from here

l=list(map(int,input().split()))
if len(l)>0:
	ma=l[0]
for i in range(len(l)):
	if ma<l[i]:
		ma=l[i]
count=[0]*(ma+1)
for i in range(len(l)):
	count[l[i]]+=1
print(l)
print(count)
for i in range(1,ma+1):
	count[i]=count[i-1]+count[i]
print(count)
l1=list(l)
print(l[len(l)-1])
print(l1)
for j in range(len(l)-1,-1,-1):
	l1[count[l[j]]-1]=l[j]
	count[l[j]]-=1
print(l1)
print(count,"updated")
