#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




#start the code from here
n=int(input())
l=list(map(int,input().split()))
m=int(input())
l1=list(map(int,input().split()))
l1c=list(l1)
a=0
b=0
ans=0
l.sort()
l1.sort()
l1c.sort()
for i in range(len(l)):
	if l[i]-1 in l1:
		ans+=1
		l1.remove(l[i]-1)
	elif l[i] in l1:
		ans+=1
		l1.remove(l[i])
	elif l[i]+1 in l1:
		ans+=1
		l1.remove(l[i]+1)

ans2=0
for i in range(len(l1c)):
	if l1c[i]-1 in l:
		ans2+=1
		l.remove(l1c[i]-1)
	elif l1c[i] in l:
		ans2+=1
		l.remove(l1c[i])
	elif l1c[i]+1 in l:
		ans2+=1
		l.remove(l1c[i]+1)
print(max(ans,ans2))


