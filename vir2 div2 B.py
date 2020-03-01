#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




t=int(input())
for i in range(t):
	r=int(input())
	l=[]
	a=[0]*10
	b=[0]*10
	c=[0]*10
	d=[0]*10

	for  j in range(r):
		st=str(input())
		l.append(st)
	se=set(l)
	if len(se)==r:
		print(0)
		for k in range(r):
			print(l[k])
		# print(se)
	else:
		cc=0
		# print(l,"qwer")
		r4=set()
		for rt in range(len(l)):
			a[int(l[rt][0])]+=1
			b[int(l[rt][1])]+=1
			c[int(l[rt][2])]+=1
			d[int(l[rt][3])]+=1
			we=len(r4)
			r4.add(l[rt])
			if we+1==len(r4):
				continue
			else:
				copyrt=l[rt]
				cc=cc+1
				elist=[]
				for y in range(4):
					elist.append(int(l[rt][y]))
				c[int(l[rt][2])]-=1
				done=0
				for ui in range(len(c)):
					if c[ui]==0:
						elist[2]=ui
						done=1
						c[ui]+=1
						break

				for i in range(len(elist)):
					elist[i]=str(elist[i])
				strtest="".join(elist)
				ccstrtes=0
				l[rt]=strtest
				for j in l:
					if j==strtest:
						ccstrtes+=1
				if ccstrtes>1:
					# print("yu")
					c[int(l[rt][2])]-=1
					elist[2]=copyrt[2]
					for ui in range(len(b)):
						if c[ui]==0:
							elist[1]=ui
							done=1
							b[ui]+=1
							break
					for i in range(len(elist)):
						elist[i]=str(elist[i])
					strtest="".join(elist)
				l[rt]=strtest
				r4.add(l[rt])
		print(cc)
		for k in range(r):
			print(l[k])







