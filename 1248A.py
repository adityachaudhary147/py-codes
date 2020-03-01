#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




#start the code from here

t=int(input())
for i in range(t):
	n=int(input())
	l=list(map(int,(input().split())))
	m=int(input())
	r=list(map(int,(input().split())))
	rodd=0
	rev=0
	lodd=0
	lev=0
	for i in range(len(r)):
		if r[i]%2==0:
			rev+=1
		else:
			rodd+=1

	for i in range(len(l)):
		if l[i]%2==0:
			lev+=1
		else:
			lodd+=1
	print(lodd*rodd+rev*lev)
