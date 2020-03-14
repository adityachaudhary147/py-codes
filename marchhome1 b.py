#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




#start the code from here
t=int(input())
st=input()
l=[]
z=0
o=0
zcount=0
lans=[]
# checkst=[]
for i in range(len(st)):
	if st[i]=="(":
		l.append(0)
		z=1
		zcount+=1
	else:
		l.append(1)
		o+=1
		# checkst+="1"

	if zcount==o:
		if sorted(l)!=l:
			lans.append(2*zcount)
		else:
			lans.append(0)
		l=[]
		zcount=0
		o=0

if len(lans)==0:
	print(-1)
else:
	print(sum(lans))
