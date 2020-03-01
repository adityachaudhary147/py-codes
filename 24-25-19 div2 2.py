#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




#start the code from here

t=int(input())
for i in range(t):
	n,p,k=map(int,input().split())
	l=list(map(int,input().split()))
	l.sort()
	b=[]
	yu=0
	for k in range(len(l)):
		if p>=l[k]:
			p=p-l[k]
			b.append(l[k])
			yu=1
		else:
			if len(b)>0:
				if yu==1:
					q=b.pop()
					if q==l[k]:
						if p-q+l[k]>=0:
							p=p-q+l[k]
							b.append(q)
							b.append(l[k])
							yu=0
						else:
							b.append(q)
					else:
						if p+q-l[k]>=0:
							p=p+q-l[k]
							b.append(q)
							b.append(l[k])
							yu=0
						else:
							b.append(q)

	print((len(b)))


