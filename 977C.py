#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




a,b=map(int,input().split())

l=list(map(int,input().split()))
l.sort()
# print(l)

try:
	if b>0:
		if b==1:
			if a>1:
				if l[0]==l[1]:
					print(-1)
				else:
					print(l[0])
			else:
				print(l[0])
		else:
			if b<a:
				if l[b]==l[b-1]:
					print(-1)
				else:
					print(l[b-1])
			else:
				print(l[b-1])
	if b==0:
		if l[0]-1>0:
			print(l[0]-1)
		else:
			print(-1)
except:
	print(-1)