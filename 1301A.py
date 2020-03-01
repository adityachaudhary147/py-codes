#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




#start the code from here

t=int(input())
for i in range(t):
	a=input()
	b=input()
	c=input()
	h=0
	for e in range(len(a)):
		if a[e]==b[e]:
			if a[e]==c[e]:
				continue
			else:
				h=1
				break
		elif b[e]==c[e] or a[e]==c[e]:
			continue
		else:
			h=1
			break
	if h==1:
		print("NO")
	else:
		print("YES")