#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




#start the code from here

t=int(input())
for i in range(t):
	n=int(input())
	# n,k1,k2=map(int,input().split())
	# lk1=list(map(int,input().split()))
	lk2=list(map(int,input().split()))
	# print(lk1,lk2)
	l=0
	r=n-1
	h=0
	for k in range(2*n):
		try:
			if max(lk2[l:r+1])-min(lk2[l:r+1])>=r-l+1:
				h=1
				break
		except:
			break
		if lk2[l]-lk2[r]:
			l+=1
		else:
			r-=1
	if h==1:
		print("Yes")
		print(l+1,r+1)
	else:
		print("No")


