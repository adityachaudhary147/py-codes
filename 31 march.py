#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




#start the code from here
t=int(input())
for i in range(t):
	a,b,c,d=(map(int,input().split()))
	x,y,x1,y1,x2,y2=map(int,input().split())
	xf=x-a+b
	yf=y-c+d
	# print(xf,yf)
	if x1==x2 and y1==y2:
		print("NO")
		continue
	newx=abs(x2-x1)
	newy=abs(y2-y1)
	xval=1
	yval=1
	# print(x,y)

	if x1<=xf and xf<=x2 and y1<=yf and yf<=y2:
		if xf==x:
			if  x1==x2:
				if a==b and a==0 and b==0:
					xval=1
				else:
					xval=0
			else:
				xval=1
		if yf==y:
			# print("nm")
			if  y1==y2:
				if c==d and c==0 and d==0:
					yval=1
				else:
					yval=0
			else:
				yval=1
		if xval==1 and yval==1:
			print("YES")
		else:
			print("NO")

	else:
		print("NO")
		
	

