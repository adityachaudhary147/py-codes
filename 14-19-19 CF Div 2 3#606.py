#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




#start the code from here

t=int(input())
for i in range(t):
	e=input()
	o=0
	t=0
	ot=0
	l=set()
	k=0
	for jk in range(len(e)):
		qw=0
		if k<len(e)-2:
			if e[k:k+3]=="one":
				o+=1
				l.add(k+2)
				k=k+3
				continue
			elif e[k:k+3]=="two":
				t+=1
				if k<len(e)-4:
					if e[k:k+5]=="twone":
						ot+=1
						l.add(k+3)
						k=k+5
						continue
				l.add(k+2)
				qw=1
				k=k+3
				continue
		
		k=k+1

	print(o+t)
	print(*l)
