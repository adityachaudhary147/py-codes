#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




#start the code from here
t=int(input())
l=list(map(int,input().split()))
s=set(l)
if len(s)<3:
	print("NO")
	exit()
else:
	l=list(s)
	l.sort()
	h=0
	for i in range(1,len(l)):
		if l[i]-l[i-1]<=1:
			h+=1
		else:
			h=0
		if h==2:
			print("YES")
			exit()
	print("NO")
