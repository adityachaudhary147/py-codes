#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




#start the code from here
a,b=map(int,input().split())
if a==1 and b==0:
	print(1)
	exit()
if b+2>a:
	print(-1)
else:
	ans=[]
	if b==0:
		for i in range(10,10+a):
			ans.append(i+1)
	else:
		for j in range(10,10+a-b):
			ans.append(j)
		for k in range(j+1,10+a):
			if len(ans)>=2:
				ans.append(ans[-1]+ans[-2])
	print(*ans)
