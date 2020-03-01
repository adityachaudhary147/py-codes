#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




#start the code from here
t=int(input())
for i in range(t):
	r=int(input())
	a=input()
	b=list(a)
	c=set()
	cc=len(a)
	answe=len(a)
	for j in range(len(a)):
		for k in range(j+1,len(a)):
			if b[j]==b[k]:
				answe=k-j-1
				break
		if answe<cc:
			cc=answe
	wqe=len(a)-cc-1
	if wqe==-1:
		print(0)
	else:
		print(wqe)




