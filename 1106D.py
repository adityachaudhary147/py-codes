#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 



from bisect import insort
#start the code from here
n,m=map(int,input().split())
	# if n==1 and m==1:
	# 	print(1)
	# 	exit()
arr=[[] for i in range(n+1)]
for i in range(m):
	l,r=map(int,input().split())
	insort(arr[l],r)
	insort(arr[r],l)
	#arr[l].append(r)
	#arr[r].append(l)
		# print(arr)


l=[False for i in range(n+1)]
rash=[]
# print(arr)
w=1
j=0
r=[1]
while len(rash)<=n:
	try:
		ert=r.pop(0)
	except:
		break

	if l[ert]==False:
		rash.append(ert)
		l[ert]=True
		for i in arr[ert]:
			insort(r,i)
print(*rash)
