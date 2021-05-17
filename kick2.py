#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 



import bisect
#start the code from here
t=int(input())
for i in range(t):
	n,k=map(int,input().split())
	l=list(map(int,input().split()))
	maxvalue=0
	if k==1:
		arr=[]
		for u in range(1,n):
			we=l[u]-l[u-1]
			if we>maxvalue:
				maxvalue=we
			arr.append(we)
		if maxvalue%2==1:
			ans=(maxvalue//2)+1			
		else:
			ans=maxvalue//2
		arr.append(ans)
		arr.remove(maxvalue)
		ans=max(arr)
		print("Case #",end='')
		print(i+1,end="")
		print(":",ans,end="")
		print()
	
	else:
		arr=[]
		for u in range(1,n):
			we=l[u]-l[u-1]
			if we>maxvalue:
				maxvalue=we
			arr.append(we)
		
		arr.sort()
		maxvalue=arr[-1]
		# print(arr)

		for h in range(k):
			# print(maxvalue)
			if maxvalue%2==1:
				ans=(maxvalue//2)+1
				bisect.insort(arr,ans)
				bisect.insort(arr,ans-1)		
			else:
				ans=maxvalue//2
				bisect.insort(arr,ans)
				bisect.insort(arr,ans)
			arr.pop()
			maxvalue=arr[-1]
			# print(arr)
		ans=arr[-1]
		print("Case #",end='')
		print(i+1,end="")
		print(":",ans,end="")
		print()



