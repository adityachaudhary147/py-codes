# cook your dish here
#jai mata di#
import sys
# sys.stdin = open('input.in', 'r')  
# sys.stdout = open('output.out', 'w')
# gaand faad denge

# from time import perf_counter
# t_start=perf_counter()  
def solve():
	in1=sys.stdin.readline()
	n,m=map(int,in1.split())
	in2=sys.stdin.readline()
	l=list(map(int,in2.split()))
	evensetinl=0
	oddsetinl=0
	for y in range(len(l)):
		l[y]=pow(bin(l[y]).count("1"),1,2)
		if l[y]==0:
			evensetinl+=1
		else:
			oddsetinl+=1

	for i in range(m):
		p=int(sys.stdin.readline())
		setbitinp=pow(bin(p).count("1"),1,2)
		setbit=0
		ev=0
		od=0
		if setbitinp%2==0:
			ev+=evensetinl
			od+=oddsetinl
		else:
			ev+=oddsetinl
			od+=evensetinl
		sys.stdout.write(str(ev)+" "+str(od))
		print()
t=int(sys.stdin.readline())
for i in range(t):
	solve()
# t_end=perf_counter()
# print("time",t_end-t_start)