#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




#start the code from here

t=int(input())
for i in range(t):
	x,y=map(int,input().split())
	x1,y1=x,y
	n,m,k=map(int,input().split())
	ab=list(map(int,input().split()))
	cd=list(map(int,input().split()))
	ef=list(map(int,input().split()))
	abxy=[]
	op=[float(+inf)]*3
	wex,rry=[0]*3,[0]*3
	cdxy=[]
	oi=[float(+inf)]*3
	wyx,rey=[0]*3,[0]*3
	for i in range(0,2*n,2):
		e=(abs(ab[i]-x))**2+(abs(ab[i+1]-y))**2
		if e <op[0]:
			op[0]=e
			wex[0]=ab[i]
			ryy[0]=ab[i+1]
	for i in range(0,2*m,2):
		f=((abs(cd[i]-x)))**2+(abs(cd[i+1]-y))**2
		if f<oi:
			oi[0]=f
			wyx[0]=cd[i]
			rey[0]=cd[i+1]
	x,y=wex[0],rry[0]
	for i in range(0,2*m,2):
		f=((abs(cd[i]-x)))**2+(abs(cd[i+1]-y))**2
		if f<oi:
			oi[1]=f
			wex[1]=cd[i]
			ryy[1]=cd[i+1]
	x,y=wex[1],rry[1]
	for i in range(0,2*k,2):
		f=((abs(ef[i]-x)))**2+(abs(ef[i+1]-y))**2
		if f<oi:
			oi[2]=f
			wex[2]=ef[i]
			ryy[2]=ef[i+1]
	x,y=wex[0],rry[0]
	for i in range(0,2*m,2):
		f=((abs(cd[i]-x)))**2+(abs(cd[i+1]-y))**2
		if f<oi:
			oi[1]=f
			wex[1]=cd[i]
			ryy[1]=cd[i+1]
	x,y=wex[1],rry[1]
	for i in range(0,2*k,2):
		f=((abs(ef[i]-x)))**2+(abs(ef[i+1]-y))**2
		if f<oi:
			oi[2]=f
			wex[2]=ef[i]
			ryy[2]=ef[i+1]


