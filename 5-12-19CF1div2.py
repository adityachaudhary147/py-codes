#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




#start the code from here

t=int(input())
for i in range(int(t)):
	e=input()
	e=list(e)
	u=len(e)
	rt=0
	if e[0]=="?":
		if len(e)>=2:
			y1=["a","b","c","?"]
			y1.remove(e[1])
			e[0]=y1[0]
		else:
			e=['a']
	for j in range(1,u):
		if e[j]==e[j-1]:
			print("-1")
			rt=1
			break
		elif  e[j]=="?":
			y=["a","b","c","?","a","b","c","?"]
			y.remove(e[j-1])
			try:
				y.remove(e[j+1])
			except:
				wer=0	
			e[j]=y[0]
	if rt==0:
		print(*e,sep="")

