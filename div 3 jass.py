#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




#start the code from here
e=int(input())
l=list(map(int,input().split()))
r=list(l)
l.sort()
print(l,r)
for i in range(e-1):
	print(i)
	if l[i]!=r[i]:
		w=min(r[i:])
		ind=r.index(w)
		print(w,ind)