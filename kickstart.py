#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




#start the code from here
t=int(input())
for i in range(t):
	n,k,p=map(int,input().split())
	main=[]
	for j in range(n):
		l=list(map(int,input().split()))
		main.append(l)
	maxsum=0
	maxvalue=0
	invalue=0
	for k in range(p):
		invalue=0
		maxvalue=0
		for y in range(n):
			try:
				if maxvalue<=main[y][0]:
					invalue=y
					maxvalue=main[y][0]
			except:
				rt=0
		print(invalue,maxvalue)
		maxsum+=main[invalue].pop(0)
		maxvalue=0

	ans=maxsum

	print("Case #",end='')
	print(i+1,end="")
	print(":",ans,end="")
	print()
	