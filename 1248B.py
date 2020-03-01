#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




#start the code from here

n=int(input())
l=list(map(int,(input().split())))
l.sort()
r=0
if n%2==1:
	t=l[len(l)//2]
else:
	t=0
for i in range(len(l)//2):
	r+=l[i]
	t+=l[n-i-1]
print(r*r+t*t)