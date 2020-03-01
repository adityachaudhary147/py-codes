#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




#start the code from here
a,b=map(int,input().split())
ans=0
if a==1 and b==1:
	print(0)
	exit()
while a>0 and b>0:
	if a>=b:
		b=b+1
		a=a-2
	else:
		b=b-2
		a=a+1
	ans+=1
print(ans)

