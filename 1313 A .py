#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




#start the code from here


t=int(input())
for i in range(t):
	a,b,x,y=map(int,input().split())
	x=x+1
	y=y+1
	# print(a,b,x,y)
	ui=max((x-1)*(y),(x)*(y-1),(a-x+1)*(y-1),y*(a-x),(x-1)*(b-y+1),(x)*(b-y),(a-x)*(b-y+1),(a-x+1)*(b-y),a*(y-1),b*(x-1),(a-x)*b,(b-y)*a)
	if ui<0:
		ui=0
	print(ui)
