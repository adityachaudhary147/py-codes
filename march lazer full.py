#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




#start the code from here
t=int(input())
for i in range(t):
	n,q=map(int,input().split())
	# st=input()
	l=list(map(int,input().split()))
	dic=dict()
	arr=[]
	for i in range(q):
		x1,x2,y=map(int,input().split())
		cc=0
		for j in range(1,n):
			# print(j-1,x1-1,x2-1,y,"check")
			if l[j-1]<=y and l[j]>=y or l[j]<=y and l[j-1]>=y:
				if x1-1<=j-1 and x2-1>=j:
					cc+=1
					# print(j-1,x2-1,x1-1,"rt")
				# print(j,"ty")
		print(cc)


