#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




#start the code from here

t=int(input())
for i in range(t):
	r=int(input())
	if r>=3:
		if r%2:
			print(1)
		else:
			print(0)
	else:
		if r==2:
			print(2)
		elif r==1:
			print(3)