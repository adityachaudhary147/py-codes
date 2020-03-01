#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




start the code from here

t=int(input())
for i in range(t):
	y=int(input())
	l=[i for i in range(1,y+1)]
	r=list(l)
	u=list(map(int,input().split()))
	result=[-1 for i in range(1,y+1)]
	# for i in range(y):
	# 	for j in range(y):
	# 		r[u[j]-1]=l[j]
	# 	bh=0
	# 	for k in range(y):
	# 		if result[k]==-1:
	# 			if r[k]==k+1:
	# 				result[k]=i+1
	# 		else:
	# 			bh+=1
	# 	if bh==y:
	# 		break
	# 	l=list(r)
	# 	print(r,"qwe")
	# print(*result)
	uio=[0]*y
	uio[0]=1
	yu=u[0]
	uio[yu-1]=1
	count=1
	lrad=[1,yu]
	for i in range(1,y+1):
		if uio[i]==0:
			while yu!=i:
				yu=u[yu-1]
				uio=1
				lrad.append(yu)
		else:
			for j in lrad:



