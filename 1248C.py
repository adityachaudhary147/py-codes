#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




#start the code from here
def fib(n):
	a=0
	b=1
	for i in range(n):
		c=a+b
		a=b
		b=c
	return c
l=list(map(int,(input().split())))
a=0
b=0
a=fib(l[0])
b=fib(l[1])
print(a,b)
print(2*(a+b-1))








