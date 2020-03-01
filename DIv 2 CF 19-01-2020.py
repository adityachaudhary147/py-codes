#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 



def binarySearch(arr, l, r, x): 
  
    while l <= r: 
  
        mid = l + (r - l)//2; 
          
        # Check if x is present at mid 
        if arr[mid] == x: 
            return mid 
  
        # If x is greater, ignore left half 
        elif arr[mid] < x: 
            l = mid + 1
  
        # If x is smaller, ignore right half 
        else: 
            r = mid - 1
      
    # If we reach here, then the element was not present 
    return -1

t=int(input())
for i in range(t):
	n,s,k=(map(int,input().split()))
	l=list(map(int,input().split()))
	s1=set(l)
	e=[]
	ans=-1
	l.sort()
	w=binarySearch(l,0,k-1,s)
	# print(w,"bin")
	if w==-1:
		print(0)
		continue
	hh1,hh2=1,1
	p1=l[w]
	p2=l[w]
	# print(l[w],"lw")
		

	while p1>0 and hh1==1:
		if p1 not in s1:
			hh1=2
			break
		p1=p1-1

	while p2<=n and hh2==1 :
		if p2 not in s1:
			hh2=2
			break
		p2=p2+1


	if hh1==2 and hh2==1:
		print(abs(s-p1))
	elif hh2==2 and hh1==1:
		print(abs(s-p2))
	elif hh2==2 and hh1==2:
		print(min(abs(s-p1),abs(s-p2)))

	
	




	


