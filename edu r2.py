#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




#start the code from here
t=int(input())
for i in range(t):
	n=int(input())
	daug=[False for j in range(n+1)]
	king=[False for k in range(n+1)]
	ans=[]
	for w in range(n):
		l=list(map(int,input().split()))
		l.pop(0)
		h=0
		for e in range(len(l)):
			if king[l[e]]==False:
				king[l[e]]=True
				daug[w+1]=True
				h=1
				break
		if h==0:
			ans.append(w+1)
		h=0
	hew=0
	# print(daug,king)
	for re in range(1,n+1):
		if king[re]==False:
			print("IMPROVE")
			print(ans[0],re)
			hew=1
			break
	if hew==0:
		print("OPTIMAL")


