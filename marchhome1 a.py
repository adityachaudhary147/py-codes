# marchhome1 a.py
#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




#start the code from here
t=int(input())
for i in range(t):
	st=int(input())
	l=list(map(int,input().split()))
	ev=[]
	od=[]
	ev1=0
	od1=0
	for i in range(len(l)):
		if l[i]%2==0:
			ev.append(i+1)
			ev1=1
			break
		elif l[i]%2==1:
			od.append(i+1)
			if len(od)>=2:
				od1=1
	if od1==0 and ev1==0:
		print(-1)
	else:
		if od1==1:
			print(2)
			print(od[0],od[1])
		else:
			print(1)
			print(ev[0])



