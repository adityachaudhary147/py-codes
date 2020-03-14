#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




#start the code from here
t=int(input())
for i in range(t):
	n,m=map(int,input().split())
	if m==2:
		type1=list(map(int,input().split()))
		price=list(map(int,input().split()))
		typeperprice=[0 for i in range(m)]
		for j in range(n):
			typeperprice[type1[j]-1]+=price[j]
		h=0
		if typeperprice[0]==0:
			print(typeperprice[1])
			h=1
		elif typeperprice[1]==0:
			print(typeperprice[0])
			h=1
		if h==0:
			if typeperprice[0]<typeperprice[1]:
				print(typeperprice[1])
			else:
				print(typeperprice[0])
	




