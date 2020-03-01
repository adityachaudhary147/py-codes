#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




#start the code from here

t=int(input())
for i in range(t):
	n=int(input())
	a=int(input())
	# sys.stdout.flush()
	s=(2*(10**n))+a
	# sys.stdout.flush()
	print(s)
	sys.stdout.flush()
	s=s-a
	# sys.stdout.flush()
	b=int(input())
	s=s-((10**n))
	print((10**n)-b)
	sys.stdout.flush()
	d=int(input())
	s=s-10**n
	print(10**n-d)
	sys.stdout.flush()

	rw=int(input())
	if rw==1:
		continue
	else:
		break



