#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




#start the code from here


t=int(input())
for y in range(t):
	a,b=map(int,input().split())
	f=abs(b-a)//5
	w=abs(b-a)%5
	if w==4 or w==3:
		f=f+2
	if w==2 or w==1:
		f=f+1
	print(f)
