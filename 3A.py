#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




#start the code from here

t=("a","b","c","d","e","f","g","h")
r=("1","2","3","4","5","6","7","8")
w=input()
init=t.index(w[0])
inir=r.index(w[1])

e=input()
fint=t.index(e[0])
finr=r.index(e[1])
qw=fint-init
ew=finr-inir
ty=max(qw,ew)
l=list()
rdy=min(qw,-ew)
ruy=min(qw,ew)
luy=min(-qw,ew)
ldy=min(-qw,-ew)
for i in range(rdy):
	l.append("RD")
	qw=qw-1
	ew+=1

for i in range(ruy):
	l.append("RU")
	qw=qw-1
	ew-=1
for i in range(luy):
	l.append("LU")
	qw=qw+1
	ew-=1
for i in range(ldy):
	l.append("LD")
	qw=qw+1
	ew+=1

if qw>0:
	for i in range(qw):
		l.append("R")
else:
	for i in range(-qw):
		l.append("L")
if ew>0:
	for i in range(ew):
		l.append("U")
else:
	for i in range(-ew):
		l.append("D")
print(len(l))
for i in range(len(l)):
	print(l[i])


