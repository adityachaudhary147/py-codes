#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 



from math import *
#start the code from here
t=int(input())
for i in range(t):
	w=int(input())
	l=set()
	l.add(0)
	r=w
	for i in range(1,int(pow(w,0.5))+1):
		yu=floor(w//i)
		l.add(i)
		l.add(yu)
		# print(i,yu)


	l=list(l)
	l.sort()

	print(len(l))
	print(*l)


