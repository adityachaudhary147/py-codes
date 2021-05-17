
#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 

def solve(A):
	l=[]
	for e in range(len(A)):
		h=e
		se=[]
		while h!=-1:
			se.append(A[h])
			h=A[h]
		l.append(se)
	ma=0
	for w in range(len(l)):
		for q in range(len(l)):
			if w!=q:
				if l[w][-1]==l[q][-1]:
					se1=set(l[w])
					se2=set(l[q])
					senew=se1.union(se2)
					inter=se1.intersection(se2)
					senew=senew.intersection(inter)
					if len(se1)>1 and len(se2)>1:
						a=len(senew)+1
					else:
						a=len(senew)
				else:
					se1=set(l[w])
					se2=set(l[q])
					se1=se1.union(se2)
					a=len(se1)
				if a>ma:
					ma=a
	return ma
h=solve([ -1, 0, 0, 1, 2, 1, 5 ])
print(h)