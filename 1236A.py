#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




#start the code from here

t=int(input())
for i in range(t):
	a,b,c=map(int,input().split())
	ans=0
	if b>c//2:
		ans=ans+(c//2)*3
		b=b-c//2
	else:
		ans=ans+b*3
		b=0
	if a>b//2:
		ans=ans+(b//2)*3
		a=a-c//2
	else:
		ans=ans+a*3
		a=0

	print(ans)
