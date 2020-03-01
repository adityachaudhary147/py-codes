#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




#start the code from here

t=int(input())
for i in range(t):
	e=int(input())
	l=list(map(int,input().split()))
	for r in range(e):
		if l[r]%2==1:
			l[r]=1
		else:
			l[r]=0
	od=l.count(1)
	ev=e-od
	if od>0 and od!=e:
		print("YES")
	elif od==e and e%2==0:
		print("NO")
	elif od==e and e%2==1:
		print("YES")
	else:
		print("NO")