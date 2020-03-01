#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




#start the code from here

t=int(input())
for i in range(t):
	e=int(input())
	l=[]
	d=dict()
	for k in range(e):
		a,b=map(int,input().split())
		d[a]=b
		l.append(a)
		l.append(b)
	l.sort()
	print(l,d)
	j=0
	a=d[l[j]]
	c=l.index(a)
	q=c
	p=c
	# while j!=q:
	# 	j=j+1
	# 	a=d[l[j]]
	# 	c=l.index(a)
	# 	if c>p:
	# 		p=c

	# print(p)



