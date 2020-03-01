#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




#start the code from here
n,m=map(int,input().split())
for i in range(n):
	strin=input()
	ans=""
	cc=0
	for r in strin:
		if r=='-':
			ans+="-"
		elif i%2==0:
			if cc%2==0:
				ans+='B'
			else:
				ans+='W'
		elif i%2==1:
			if cc%2==1:
				ans+='B'
			else:
				ans+='W'
		cc+=1
	print(ans)