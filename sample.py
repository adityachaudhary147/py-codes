#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




#start the code from here




t=int(input())
for i in range(t):
	r=int(input())
	lis=[]
	q,w=0,0
	hh=0
	dic=dict()
	for er in range(int(r)):
		e,r=map(int,input().split())
		ersum=e+r
		if ersum in dic:
			hh=2
		else:
			dic[ersum]=[e,r]
	if hh==2:
		print("NO")
		continue
	# print(dic,hh)
	qwer=sorted(dic.keys())
	# print(qwer)

	for k in qwer:
		lio=dic[k]
		# print(lio)
		# q
		e=lio[0]
		#w 
		r=lio[1]
		if e<q or r<w:
			hh=1
			break
		for j in range(e-q):
			lis.append("R")	
		for l in range(r-w):
			lis.append("U")
		q=e
		w=r
	if hh==1:
		print("NO")
		continue

	print("YES")
	print("".join(lis))

