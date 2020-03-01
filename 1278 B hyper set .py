#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




#start the code from here


n,k2=map(int,input().split())
l=set()
for i in range(n):
	e=input()
	l.add(e)
r=set(l)
l=list(l)
an=0
for j in range(n-1):
	for k in range(j+1,n):
		we=[0]*k2
		ty=0
		while ty<k2:
			if l[j][ty]==l[k][ty]:
				we[ty]=l[j][ty]
			else:
				if l[j][ty]!='E' and l[k][ty]!='E':
					we[ty]='E'
				if l[j][ty]!='T' and l[k][ty]!='T':
					we[ty]='T'
				if l[j][ty]!='S' and l[k][ty]!='S':
					we[ty]='S'
			ty+=1
		we=''.join(we)
		# print(we)
		if we in r:
			an+=1
print(an//3)




