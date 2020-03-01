#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




#start the code from here
a,b=map(int,input().split())
stack=[b]
ans=[]
h=0
while stack:
	p=stack.pop()
	ans.append(p)
	if p==a:
		break
	else:
		if p<a:
			h=1
			break
	if p%10==1:
		p=p//10
		stack.append(p)
	elif p%2==0:
		p=p//2
		stack.append(p)
	else:
		h=1
		break
ans.reverse()
if h==1:
	print("NO")
else:
	print("YES")
	print(len(ans))
	print(*ans)