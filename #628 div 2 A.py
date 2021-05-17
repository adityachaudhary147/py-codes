#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




#start the code from here
t=int(input())
for i in range(t):
	e=int(input())
	if e%2==0:
		print(e//2,e//2)
	else:
		if (e//2)%2==0:
			print((e-2)//2,2)
		else:
			print(e//2,2)

