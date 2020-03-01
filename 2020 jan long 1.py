#jai mata di#
import sys
sys.stdin = open('input.in', 'r')
sys.stdout = open('output.out', 'w')



t=int(input())
for i in range(t):
	q=int(input())
	l=set()
	an=0
	for j in range(q):
		y=str(input())
		e=len(l)
		l.add(y)
		if len(l)==e:
			l.remove(y)
			an+=(len(y))**2
	# print(l)
	w=list(l)
	w.sort()
	k=0
	# print(w,an)
	while k<len(w):
		r=0
		r1=-1
		r1c=0
		qw=0
		qw1=-1
		qw1c=0
		hh=0
		try:
			while w[k][r]==w[k+1][r]:
				r=r+1
			while w[k][r1]==w[k+1][r1]:
				r1c+=1
				r1-=1

			while w[k+1][qw]==w[k+2][qw]:
				qw=qw+1
			while w[k+1][qw1]==w[k+2][qw1]:
				qw1c+=1
				qw1-=1

			
		except:
			er=0
		if qw1<qw:
			qw=qw1
		if r1c<r:
			r=r1c
		if qw>r:
				hh=1
				r=qw

		if hh==1:
			k=k+3
		else:
			k=k+2

		an+=r*r
	print(an)
