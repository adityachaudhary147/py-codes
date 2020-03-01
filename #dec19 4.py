#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 

import  math

import math
#start the code from here

t=int(input())
for i in range(t):
	e=int(input())
	q=list(input())
	p=list(input())
	cq1=q.count('1')
	cq0=e-cq1
	cp1=p.count('1')
	cp0=e-cp1
	rew=min(cq0,cp1)+min(cq1,cp0)
	maxone=rew
	rew2=min(cq0,cp0)+min(cq1,cp1)
	minone=e-rew2
	answer=0
	for k in range(minone,maxone+1,2):
		if e==2*k:
			answer+=math.factorial(e)//(math.factorial(k)**2)
			continue
		answer+=math.factorial(e)//(math.factorial(k)*(math.factorial(e-k)))
	print(pow(answer,1,1000000007))
