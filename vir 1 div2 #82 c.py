#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




#start the code from here

n,m,c,d=map(int,input().split())
l=[[d,c]]
for i in range(m):
	a,b,e,f=map(int,input().split())
	l.append([f,a,b,e])
l.sort(reverse=True)
# print(l)
prof=0
dp=[]
for j in range(len(l)):
	for i in range(len(l)):
		if len(l[i])==4:
			w=min(l[i][1]//l[i][2],n//l[i][3])
			prof+=w*l[i][0]
			dp.append(w*l[i][0])
			# l[i][1]-=w*l[i][2]
			# n=n-w*l[i][3]
		else:
			w=n//l[i][1]
			prof+=w*l[i][0]
			dp.append(w*l[i][0])
			# n=n-w*l[i][1]
	
print(dp)


