# 706B dp.py
#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




#start the code from here
def bins(er,l,r,val):
	mid=(l+r)//2
	# print(l,r,mid)
	y,e=l,r
	if l<r:
		if er[mid]==val:
			return mid+1
		elif er[mid]>val:
			r=mid
			if e==r and y==l:
				return mid
			return bins(er,l,r,val)
		elif er[mid]<val:
			l=mid
			if y==l and e==r:
				return mid
			return bins(er,l,r,val)
	else:
		return mid+1



n=int(input())
l=list(map(int,input().split()))
q=int(input())
l.sort()
print(l)
for i in range(q):
	q1=int(input())
	print(bins(l,0,n-1,q1))
