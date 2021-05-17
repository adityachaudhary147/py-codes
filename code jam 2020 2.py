#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 



# created by Aditya Chaudhary
# shut the fuck up
#start the code from here
t=int(input())
for i in range(t):
	n=int(input())
	C=[]
	J=[]
	arr=[]
	dic=dict()
	for w in range(n):
		a,b=map(int,input().split())
		dic[(a,b)]=w
		arr.append([a,b])
	arr.sort()
	ans=['' for i in range(n)]
	
	# print(arr)
	C.append(arr[0])
	a,b=arr[0][0],arr[0][1]
	ind=dic[(a,b)]
	ans[ind]+='C'
	h=0
	whend=0
	for w in range(1,n):
		h=0
		# for C
		end=C[-1][1]
		stnew=arr[w][0]
		if stnew>=end:
			h=1
			C.append(arr[w])
			a,b=arr[w][0],arr[w][1]
			ind=dic[(a,b)]
			print(ans,type(ans[ind]))
			ans[ind]+='C'
		# if j needs
		if h==0:
			if len(J)==0:
				J.append(arr[w])
				a,b=arr[w][0],arr[w][1]
				ind=dic[(a,b)]
				ans[ind]+='J'
				continue
			else:
				end=J[-1][1]
				stnew=arr[w][0]
				if stnew>=end:
					J.append(arr[w])
					a,b=arr[w][0],arr[w][1]
					ind=dic[(a,b)]
					ans[ind]+='J'
					continue
				else:
					whend=1
	if whend==1:
		ans=["IMPOSSIBLE"]
	# print(C,J)




	print("Case #",end='')
	print(i+1,end="")
	print(":","".join(ans),end="")
	print()

