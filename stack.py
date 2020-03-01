#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




#start the code from here
global l,n,top
l=[]
n=10
top=0
def stackpush(l,item):
	global n,top
	if  len(l)<n:
		l.append(item)
		top=top+1
	else:
		print("overflow")
def stackpop(l,item):
	global n,top 
	if len(l)==0:
		return print("underflow")
	else:
		top=top-1
		return l.pop()
		
def stackshowall(l):
	global n,top
	r=top
	for i in range(r-1,-1,-1):
		print(l[i])
#can not define a new stack so we will use class and object to do so 
stackpush(l,10)
stackpush(l,14)
stackpush(l,17)
stackpush(l,19)
e=0
r=stackpop(l,e)
print(r,"poped item ")

stackpush(l,100)
stackshowall(l)

