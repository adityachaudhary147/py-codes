#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




#start the code from here
t=int(input())
l1=list(map(int,input().split()))
cc=0
val=[[-1 for i in range(t+1)] for j in range(t+1)]
for i in range(t):
	if l[i]!=0:
		val[i][i]=l[i]
		cc+=1
		l.append(val[i][i])

# print(dp)
sump=list(l)
for i in range(1,t):
	sump[i]+=sump[i-1]
# print(sump)
# print(cc)
if cc==0 or cc==1:
	print(cc)
	exit()
t=len(l)
gi,gj=-1,-1
flag=[True for i in range(2*t)]

for w in range(2,len(l)+1):
	for i in range(t-w+1):
		j=i+w-1
		val[i][j]=val[i][j-1]+l[j]
		if val[i][j-1]==0:
			val[i][j]=0
		if val[i][j]!=0:
			cc+=1
			

			
print(cc)