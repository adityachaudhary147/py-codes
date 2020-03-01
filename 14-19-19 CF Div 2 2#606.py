#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 



from math import *
#start the code from here

t=int(input())
for i in range(t):
	e=int(input())
	l=[]
	for k in range(e):
		a=input()
		l.append(a)
	q=[]
	hh=0
	for j in range(1,e):
		if l[j-1][-1]==l[j][0]:
			continue
		else:
			q.append(j+1)
			if l[j-1][-1]==l[j-1][0] and l[j-1][-1]==l[j-1][0]:
				hh=1
				break
	h=[]
	if hh!=1:
		if len(q)>0:
			if q[-1]!=e:
				hh=1
	if hh!=1:
		for w in range(0,len(q),2):
			h.append(q[w])
		print(len(h))
		print(*h)
	else:
		print(-1)