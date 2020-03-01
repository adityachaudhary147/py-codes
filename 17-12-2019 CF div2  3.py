#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




#start the code from here

a,b=(map(int,input().split()))
if a==1 and b==1:
	print(0)
else if a==1:
	for i in range(a):
		print(1)
