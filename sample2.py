#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 





import math      
t=int(input())
for i in range(t):
	n=int(input())
	cnt = 0
	l=[]
	r=[]
	for i in range(1, (int)(math.sqrt(n)) + 1):
		if (n % i == 0) :
			l.append(i)
			r.append(i)
			if (n / i == i):
				cnt = cnt + 1
			else:
				l.append(n//i)
				cnt=cnt+2

	if cnt>=6 and len(r)>3:
		print("YES")
		print(r[1],r[2],n//(r[1]*r[2]))
	else:
		print("NO")


