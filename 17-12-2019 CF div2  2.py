#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




#start the code from here

t=int(input())
l=list(map(int,input().split()))
for i in range(len(l)):
	qw=pow(l[i],1,14)
	if qw<7 and qw>0 and l[i]>14:
		print("YES")
	else:
		print("NO")
