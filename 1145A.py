#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




#start the code from here
# t=int(input())
# st=input()
# l=list(map(int,input().split()))
# a,b=map(int,input().split())
# for i in range(t):

n=int(input())
l=list(map(int,input().split()))
ca=[]
def fun(l,left,right):
	f=True
	for i in range(left,right-1):
		if l[i]<=l[i+1]:
			f=True
		else:
			f=False
			break
	mid=(left+right)//2		
	if f==True:
		return right-left
	else:
		return max(fun(l,left,mid),fun(l,mid,right))
print(fun(l,0,n))