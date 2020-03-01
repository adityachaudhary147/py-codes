#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




#start the code from here
def heapify(l,n,i):
	j=i #root
	left=2*i+1
	right=2*i+2
	if left<n and l[left]>l[j]:
		j=left
	if right<n and l[right]>l[j]:
		j=right
	if j!=i:
		l[i],l[j]=l[j],l[i]
		# print(l[i],l[j])
		# print(l[j],l[i])
		heapify(l,n,j)
	# print(l)

def heapsort(l):
	n=len(l)
	for i in range(len(l)):
		heapify(l,n,i)
	print(l,"in heapsort")
	for i in range(len(l)):
		l[0],l[n-i-1]=l[n-i-1],l[0]
		# print(l,"first")
		heapify(l,n-i-1,0)
		# print(l,"first2")







l=list(map(int,input().split()))
l=[3,12,4,7,6,2,1,9]
heapsort(l)
# heapify(l,len(l),0)
print(l)





