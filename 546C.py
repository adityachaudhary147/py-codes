#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




#start the code from here
t=int(input())
l=list(map(int,input().split()))
l1=list(map(int,input().split()))
k1=l.pop(0)
k2=l1.pop(0)
game=0
h=0
len10=1
len20=1
while len(l)!=0 and len(l1)!=0:
	a=l.pop(0)
	b=l1.pop(0)
	if a>b:
		l.append(b)
		l.append(a)
	elif b>a:
		l1.append(a)
		l1.append(b)
	game+=1
	if game>10000:
		h=1
		break
	if len(l)==0:
		len10=0
	if len(l1)==0:
		len20=0
if h==0:
	print(game,end=" ")
	if len20:
		print(2)
	if len10:
		print(1)
else:
	print(-1)
