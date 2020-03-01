#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




#start the code from here

t=int(input())
for i in range(int(t)):
	e=int(input())
	l=list(map(int,input().split()))
	cc=0
	on,onb,teo=0,0,0
	for y in range(int(e)):
		if l[y]==0:
			onb+=1
		if l[y]==2:
			teo+=1
	if onb>1:
		cc+=((onb-1)*onb)//2
	if teo>1:
		cc+=((teo-1)*teo)//2
	print(cc)
