#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 



a,b=map(int,input().split())
strin=input()
st=0
ans=0
while True:
	if st+1==len(strin):
		break
	elif st+1>len(strin):
		st=st-1
	else:
		w=st
		w=w+b
		h=0
		if w+1>len(strin):
			w=len(strin)-1
		while w!=st:
			if strin[w]=='1':
				ans+=1
				h=1
				break
			else:
				w=w-1			
		if h==0:
			print(-1)
			break
		else:
			st=w
if h==1:
	print(ans)
