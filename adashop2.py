#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




#start the code from here
t=int(input())
for i in range(t):
	r0,c0=map(int,input().split())
	if r0==1 and c0==1:
		print(25)
		r0+=1
		c0+=1
		while r0<=4 and c0<=4:		
			
			print(r0,c0)
			if r0+c0-1<=8:
				print(1,r0+c0-1)
			else:
				print(1,8)
			if r0+c0-1<=8:
				print(r0+c0-1,1)
			else:
				print(8,1)
			print(r0,c0)
			r0+=1
			c0+=1
		r0-=1
		c0-=1
		# print()

		while r0>1 and c0>1:		
			
			print(9-r0,9-c0)
			print(9-1,9-(r0+c0-1))
			print(9-(r0+c0-1),9-1)
			print(9-r0,9-c0)
			r0-=1
			c0-=1
		print(8,8)

