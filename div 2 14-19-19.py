#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




#start the code from here
t=int(input())
for i in range(t):
	e=input()
	l=len(e)
	ans=0
	if l==1:
		print(e)
	else:
		ans=(len(e)-1)*9
		f=e[0]
		qw=f*len(e)
		qw=int(qw)
		e=int(e)
		if qw>e:
			ans+=int(f)-1
		else:
			ans+=int(f)
		print(ans)