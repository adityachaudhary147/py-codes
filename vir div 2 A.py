#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




# start the code from here
t=int(input())
# st=input()
# l=list(map(int,input().split()))
# a,b=map(int,input().split())
for i in range(t):
	l=list(map(int,input().split()));
	ma=max(l);
	l.remove(ma);
	ma2=max(l);
	l.remove(ma2);
	b=ma-ma2;
	ans=0
	if b>l[0]:
		ma=ma-l[0]
		ans+=l[0]
		l[0]=0
	else:
		l[0]=l[0]-b
		ma=ma-b
		ans+=b
	b=ma-ma2
	# print(ma,ma2,l[0],ans)
	if b==0:
		if l[0]%2==1:
			if b==0:
				ans+=l[0]//2
				ma=ma-l[0]//2
				ans=ans+l[0]//2+1
				ma2=ma2-l[0]//2-1
				ans+=min(ma2,ma)
		else:
			if b==0:
				ans+=l[0]//2
				ma=ma-l[0]//2
				ans=ans+l[0]//2
				ma2=ma2-l[0]//2
				ans+=min(ma2,ma)
		print(ans)
	else:
		ans+=min(ma,ma2)
		print(ans)

		


