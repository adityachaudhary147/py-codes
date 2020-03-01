#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 



from collections import Counter
#start the code from here
t=int(input())
l=list(map(int,input().split()))
l.sort()
c=Counter(l)
l1=list(c)
h=1
cc=0
# print(c)
while h>0:
	h=0
	for i in l1:
		if c[i]>0:
			c[i]-=1
			h+=1
	if h>0:
		cc+=h-1
	# print(c,h,cc)
	# print(h)
print(cc)
