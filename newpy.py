#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




#start the code from here

t=int(input())
tot=0
for i in range(t):
	n=int(input())
	arr=[[0 for i in range(4)] for j in range(4)]
	ppd=0
	for j in range(n):
		n,m=map(str,input().split())
		if n=='A':
			if m=='3':
				arr[0][0]+=1
			if m=='6':
				arr[0][1]+=1
			if m=='9':
				arr[0][2]+=1
			if m=='12':
				arr[0][3]+=1

		if n=='B':
			if m=='3':
				arr[1][0]+=1
			if m=='6':
				arr[1][1]+=1
			if m=='9':
				arr[1][2]+=1
			if m=='12':
				arr[1][3]+=1

		if n=='C':
			if m=='3':
				arr[2][0]+=1
			if m=='6':
				arr[2][1]+=1
			if m=='9':
				arr[2][2]+=1
			if m=='12':
				arr[2][3]+=1


		if n=='D':
			if m=='3':
				arr[3][0]+=1
			if m=='6':
				arr[3][1]+=1
			if m=='9':
				arr[3][2]+=1
			if m=='12':
				arr[3][3]+=1
	ppd2=0
	we=[0,0,0,0]
	arrlen=[]
	for r in range(4):
		for o in range(4):
			arrlen.append(arr[r][o])
	# print(arr,arrlen)
	sd1=0
	pattern=[[0,5,10,15],[0,5,11,14],[0,9,6,15],[0,9,7,14],[0,13,6,11],[0,13,7,10]]


	for yu in range(24):
		we[0]=arrlen[pattern[sd1][0]]
		we[1]=arrlen[pattern[sd1][1]]
		
		we[2]=arrlen[pattern[sd1][2]]
		
		we[3]=arrlen[pattern[sd1][3]]
		ppd2=0

		we.sort()
		r=[25,50,75,100]
		for ry in range(4):
			if we[ry]==0:
				ppd2=ppd2-100
			else:
				ppd2+=we[ry]*r[ry]
		if ppd2>0:
			if ppd2>ppd:
				ppd=ppd2
		else:
			if ppd==0:
				ppd=ppd2
			elif ppd2>ppd:
				ppd=pp
		sd1+=1
		if sd1==6:
			sd1=0
			q_1=arrlen.pop(0)
			q_2=arrlen.pop(0)
			q_3=arrlen.pop(0)
			q_4=arrlen.pop(0)
			arrlen.append(q_1)
			arrlen.append(q_2)
			arrlen.append(q_3)
			arrlen.append(q_4)
	print(ppd)
	tot+=ppd
print(tot)





