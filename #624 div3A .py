#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




#start the code from here


t=int(input())
for i in range(t):
	# l=list(map(int,input().split()))
	# r=int(input())
	# for j in range(r):
	a,b=map(int,input().split())
	l=list(map(int,input().split()))
	arr=list(map(int,input().split()))
	lcopy=list(l)
	# # lcopy.sort()
	# arr.sort(reverse=True)
	# for j in range(len(arr)):
	# 	if (l[arr[j]-1])>(l[arr[j]]):
	# 		l[arr[j]-1],l[arr[j]]=l[arr[j]],l[arr[j]-1]
	# 		print(l[arr[j]],l[arr[j]-1])
	# h=0
	# print(l,lcopy)
	arrcopy=set()
	for u in range(len(l)):
		for j in range(0,len(l)-u-1):
			if lcopy[j]>lcopy[j+1]:
				lcopy[j],lcopy[j+1]=lcopy[j+1],lcopy[j]
				arrcopy.add(j+1)
	arr=set(arr)
	if len(arrcopy-arr)==0:
		print("YES")
	else:
		print("NO")
	# arr=list(arr)
	# arrcopy=list(arrcopy)
	# arrcopy.sort()
	# print(arrcopy,arr)
	# h=0
	# if len(arrcopy)==len(arr):
	# 	for r in range(len(arr)):
	# 		if arr[r]==arrcopy[r]:
	# 			continue
	# 		else:
	# 			h=1
	# 			break
	# 	if h==1:
	# 		print("NO")
	# 	else:
	# 		print("YES")
	# else:
	# 	print("NO")