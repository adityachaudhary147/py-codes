#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




#start the code from here
t=int(input())
l=list(map(int,input().split()))
l.reverse()
# print(l)
stack=[]
s=len(stack)
w=-1
e=0
while True:
	try:
		# print(stack)
		if len(stack)==0:
			stack.append(l[e])
			e=e+1
		else:
			if stack[-1]==l[e]:
				qw=stack.pop()
				l[e]=qw+1
				h=1
				# e=e+1
			else:
				stack.append(l[e])
				e=e+1
	except:
		break
# print(stack)
print(len(stack))















