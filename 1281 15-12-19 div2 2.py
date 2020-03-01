#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




#start the code from here

t=int(input())
for i in range(t):
	l=list(map(str,input().split()))
	# print(l)

	for k in range(len(l[0])):
		r=[l[0][k]]
		h=0
		e=[]
		kl=[]
		for j in range(k+1,len(l[0])):
			if len(r)==1:
				if r[-1]>l[0][j]:
					r.append(l[0][j])
					h=1
					e.append(j)
					kl.append(k)
			if len(r)>1:
				if r[-1]>=l[0][j]:
					r.append(l[0][j])
					h=1
					e.append(j)
					kl.append(k)
		if h==1:
			break
	# print(r)
	# print(e,"adi")
	# print(kl)
	# print(l[0])
	a2=list(l[0])
	if len(r)>1:
		a2[kl[-1]],a2[e[-1]]=a2[e[-1]],a2[kl[-1]]
		l[0]="".join(a2)
	if l[1]>=l[0]:
		print(l[0])
	else:
		print("---")