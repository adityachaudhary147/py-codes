#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 
#start the code from here




t=int(input())
for i in range(t):
	e,m,k=map(int,input().split())
	st=list(map(int,input().split()))
	e1=st[:m]
	e2=st[e-m:]
	# print(e1,e2)
	tyu=0
	for y in range(1,m):
		if y<=k and y<m:
			if st[0]>st[-1]:
				l=st.pop()
			else:
				l=st.pop(0)
		if y==m and y<=k:
			if st[0]<st[-1]:
				print(st.pop())
			else:
				print(st.pop(0))
			tyu=1
			break

	# print(st)
	if tyu==0:
		m=m-k-1
		e1e=st[:m]
		e2e=st[(e-k)-m:]
		er1=0
		er2=0


		if len(e1)>0:
			a=min(e1)
			e1=1
		if len(e2)>0:
			b=min(e2)
			e2=1
		if e1==1 and e2==1:
			print(min(a,b))
		elif e1==1:
			print(a)
		elif e2==1:
			print(b)
