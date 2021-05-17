#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




#start the code from here
t=int(input())
for i in range(t):
	n,k,p=(map(int,input().split()))
	main=[]
	for u in range(t):
		l=list(map(int,input().split()))
		for e in range(1,len(l)):
			l[e]=l[e-1]+l[e]
		main.append(l)
	print(main)
	ans=[]
	l=[0]
	for w in range(k):
		l.append(main[0][w])
	ans.append(l)
	print(ans)
	for r in range(1,n):
		l=[0]
		for y in range(k):
			




