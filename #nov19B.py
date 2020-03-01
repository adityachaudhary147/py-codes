#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




#start the code from here

t=int(input())
for i in range(t):
	r=int(input())
	y=(input())
	y=int(y,2)
	for i in range(r-1):
		e=(input())
		e=int(e,2)
		u=bin(y^e)
		o=u
		y=int(u,2)
	print(o.count("1"))

		
