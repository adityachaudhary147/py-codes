#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




#start the code from here



def mergesort(l,i,j):
	m=(i+j)//2
	if j-i>0:
		mergesort(l,i,m)
		mergesort(l,m+1,j)
		merge(l,i,m,j)

def merge(l,a,m,b):
	if b-a>0:

		left=l[a:m+1]
		right=l[m+1:b+1]
		j,k,i=0,0,a
		while j<len(left) and k<len(right):
			if left[j]<right[k]:
				l[i]=left[j]
				j=j+1
				i=i+1

			else:
				l[i]=right[k]
				k=k+1
				i+=1
		while j<len(left):
			l[i]=left[j]
			j=j+1
			i+=1
		while k<len(right):
			l[i]=right[k]
			k=k+1
			i+=1



l=list(map(int,input().split()))
l=[3,12,4,7]
mergesort(l,0,3)
print(l)





