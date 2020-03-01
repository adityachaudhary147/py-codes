#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




#start the code from here

t=int(input())
l=[]
for i in range(t):
	a,b,c,cost=map(int,input().split())
	l.append([cost,i+1,a,b,c])
am=0;bm=0;cm=0;
if a>=am and b>=bm and c>=cm:
	am=a;bm=b;cm=c;
for i in range(t):
	am=l[i][2];bm=l[i][3];cm=l[i][4];
	for j in range(t):
		a=l[j][2];b=l[j][3];c=l[j][4];
		if a<am and b<bm and c<cm:
			l[j][0]=1111;
l.sort()
print(l[0][1])
			
		
# print(l)