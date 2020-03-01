# 1271A
#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




#start the code from here

a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
f=int(input())
prof=0
if e>f:
	w=min(a,d)
	prof+=w*e
	a=a-w
	d=d-w
	w=min(b,c,d)
	prof+=w*f
	b=b-w
	c=c-w
	d=d-w
	print(prof)
else:
	w=min(b,c,d)
	prof+=w*f
	b=b-w
	c=c-w
	d=d-w
	w=min(a,d)
	prof+=w*e
	a=a-w
	d=d-w
	print(prof)
