#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




#start the code from here

def recur(a,b,l,h):
	if a[(h+l)//2]==b:
		return q//2
	elif a[(h+l)//2]>b:
		return recur(a,b,0,(l+h)//2)
	elif a[(h+l)//2]>b:
		return recur(a,b,(l+h)//2,h)

n=int(input())
l=list(map(int,input().split()))
q=int(input())
l1=list()
for i in range(q):
	e=int(input())
	l1.append(e)
for i in range