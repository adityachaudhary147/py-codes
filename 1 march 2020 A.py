#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




#start the code from here
n=int(input())
l=list(map(str,input().split()))
l1=list(map(str,input().split()))
a="".join(l)
b="".join(l1)
a1=int(a,2)
b1=int(b,2)
if a1==b1:
	print(-1)
	exit()
q=str(bin(a1&b1))
w=a.count("1")-q.count("1")
ans=0
if w!=0:
	ans=(b.count("1")-q.count("1"))//(a.count("1")-q.count("1"))+1
else:
	print(-1)
	exit()
if ans>0:
	print(ans)
elif ans==0:
	print(1)
else:
	print(-1)