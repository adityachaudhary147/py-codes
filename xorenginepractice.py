#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w')
# gaand faad denge
from time import perf_counter
t_start=perf_counter()  
it =[0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4]  
def count(x): 
    hexnum = 0 
    if(0 == x): 
        return it[0]
    hexnum =x&0xf 
    return it[hexnum] + count(x>>4)
def solve():
	in1=sys.stdin.readline()
	n,m=map(int,in1.split())
	in2=sys.stdin.readline()
	l=list(map(int,in2.split()))
	for i in range(m):
		p=int(sys.stdin.readline())
		setbit=0
		ev=0
		od=0
		for j in l:
			setbit=count(j^p)
			if setbit%2==0:
				ev+=1
			else:
				od+=1
		sys.stdout.write(str(ev)+" "+str(od))
		print()
t=int(sys.stdin.readline())
for i in range(t):
	solve()
t_end=perf_counter()
print("time",t_end-t_start)