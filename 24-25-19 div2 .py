#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




#start the code from here

#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




#start the code from here

t=int(input())
for i in range(t):
	a,b,c,r=map(int,input().split())
	if b<a:
		b,a=a,b
	if c+r<a and c+r<b:
		ans=(abs(b-a))
	elif a<c-r and b<c-r:
		ans=(abs(b-a))
	elif  a<=c+r and a>=c-r:
		ans=(abs(b-a)-abs(c+r-a))
	elif  b<=c+r and b>=c-r:
		ans=abs(b-a)-abs(c-r-b)
	else:
		ans=abs(b-a)-2*r
	if ans>0:
		print(ans)
	else:
		print(0)