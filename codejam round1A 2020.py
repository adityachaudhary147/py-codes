#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




#start the code from here
t=int(input())
for i in range(t):
	st=int(input())
	l=[]
	m=0
	ind=0
	ans1=""
	ans2=""
	for e in range(st):
		s=input()
		l.append(s)
		ma=len(s)
		w=""
		w2=""
		h=0
		for u in range(len(s)):
			if h==0:
				if s[u]!="*":
					w+=s[u]
				else:
					h=1
			if h==1:
				if s[u]!="*":
					w2+=s[u]

		if len(ans1)<len(w):
			ans1=w
		if len(ans2)<len(w2):
			ans2=w2



		if ma>m:
			m=ma
			ind=e
	ans=ans1+"*"+ans2
	res=True
	for e in range(len(l)):
		for w in range(len(l[e])):
			if ans[w]==l[e][w]:
				if l[e][w]=="*":
					break
			else:
				if l[e][w]=="*":
					break
				res=False
				break
	if res==False:
		print("Case #",end='')
		print(i+1,end="")
		print(":","*",end="")
		print()
	else:
		res=True
		for e in range(len(l)):
			j=-1
			for w in range(len(l[e])-1,-1,-1):
				if ans[j]==l[e][w]:
					# print(ans[j],l[e][w])

					if ans[j]=="*":
						break
				else:
					if l[e][w]=="*":
						break
					res=False
					break
				j=j-1

		if res==False:
			print("Case #",end='')
			print(i+1,end="")
			print(":","*",end="")
			print()
		else:
			ans1=""
			for e in ans:
				if e!="*":
					ans1+=e
			# print(ans1)

			print("Case #",end='')
			print(i+1,end="")
			print(":",ans1,end="")
			print()
