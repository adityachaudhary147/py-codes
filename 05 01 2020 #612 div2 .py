#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




#start the code from here

n,m=map(int,input().split())
q=[]
for i in range(n):
	l=input()
	l1=[]
	for j in range(int(m)):
		if l[j]=="S":
			l1.append("1")
		elif l[j]=="E":
			l1.append("2")
		elif l[j]=="T":
			l1.append("3")
	l1="".join(l1)
	l1=int(l1)
	q.append(l1)

for i in range()


 