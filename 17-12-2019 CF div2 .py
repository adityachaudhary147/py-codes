#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




#start the code from here
t=int(input())
w=0
for k in range(t):
	a=input()
	a=list(a)
	l=[0 for i in range(10)]
	evv=0
	for i in range(len(a)):
		if a[i]=="0":
			l[0]+=1
			evv+=1
		if a[i]=="1":
			l[1]+=1
		if a[i]=="2":
			l[2]+=1
			evv+=1
		if a[i]=="3":
			l[3]+=1
		if a[i]=="4":
			l[4]+=1
			evv+=1
		if a[i]=="5":
			l[5]+=1
		if a[i]=="6":
			l[6]+=1
			evv+=1
		if a[i]=="7":
			l[7]+=1
		if a[i]=="8":
			l[8]+=1
			evv+=1
		if a[i]=="9":
			l[9]+=1
	sumn=0
	for w in range(0,10):
		sumn+=l[w]*w
	qw=0
	if l[0]>=1 and evv>=2:
		if sumn%3==0:
			print("red")
			qw=1
	if qw==0:
		print("cyan")
		


