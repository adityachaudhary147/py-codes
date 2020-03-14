#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




#start the code from here
t=int(input())
l=list(map(int,input().split()))
l.sort()
# print(l)
parent=[i for i in range(t)]
for i in range(t):
	for j in range(t):
		if i!=j:
			if l[j]*3==l[i]:
				parent[j]=i
			if l[i]*2==l[j]:
				parent[j]=i
lis=[]
# print(parent)
for y in range(t):
	if y==parent[y]:
		lis.append(y)
# print(lis)

print(l[lis[0]],end=" ")
e=l[lis[0]]
for i in range(len(l)-1):
	if (2*e) in l:
		print(2*e,end=" ")
		e=2*e
	else:
		print(e//3,end=" ")
		e=e//3
