#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




#start the code from here
n,q=map(int,input().split())
l=[0]*(10**5)
for i in range(n):
	w=int(input())
	p=0
	if l[w]==0:
		if w==p:
			l[p]=1
			if l[p+1]==0:
				p=p+1
		elif w-q>=0:
			if l[w-q]==0:
				l[w-q]=1
			else:
				l[w-q]




