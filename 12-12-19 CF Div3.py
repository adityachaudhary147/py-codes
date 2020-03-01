#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




#start the code from here

t=int(input())
for i in range(t):
	l=list(map(int,input().split()))
	l.sort()
	# mi=abs(l[1]-l[0])+abs(l[2]-l[1])+abs(l[2]-l[0])
	if l[0]==l[1]==l[2]:
		mi=0
	elif l[0]==l[1]:
		l[2]=l[2]-1
		if l[2]==l[0]:
			mi=0
		else:
			l[1]+=1
			l[0]+=1
			mi=2*abs(l[2]-l[0])
	elif l[1]==l[2]:
		l[0]+=1
		if l[0]==l[1]:
			mi=0
		else:
			l[1]-=1
			l[2]-=1
			mi=2*abs(l[0]-l[1])
	else:
		if l[2]-l[1]==1:
			l[2]-=1
			l[0]+=1
			mi=2*abs(l[2]-l[0])
		elif l[1]-l[0]==1:
			l[0]+=1
			l[2]-=1
			mi=2*(abs(l[2]-l[1]))
		else:
			l[0]+=1
			l[2]-=1
			mi=abs(l[1]-l[0])+abs(l[2]-l[1])+abs(l[2]-l[0])
	print(mi)
