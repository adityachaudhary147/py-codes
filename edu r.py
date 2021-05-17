#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




#start the code from here
t=int(input())
for i in range(t):
	a,b=map(int,input().split())
	new=a**0.5
	# print(int(new))
	new=int(new)
	if a-new!=0:
		anew=a-new
		if anew%2==0:
			ahkf=0
		else:
			new=new-1
	if new%2==0:
		if b<=new and b%2==0:
			print("YES")
		else:
			print("NO")
	else:
		if b<=new and b%2==1:
			print("YES")
		else:
			print("NO")