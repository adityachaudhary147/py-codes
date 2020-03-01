#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output(1).out', 'w') 




#start the code from here

t=int(input())
for i in range(t):
	e=input()
	e1=input()
	w=int(e,2)
	w1=int(e1,2)
	#print(w,w1) 
	cc=0
	while w1>0:
		r=w^w1
		r1=w&w1
		#print(bin(r),bin(r1))
		w=r
		w1=r1*2
		cc+=1
	print(cc)