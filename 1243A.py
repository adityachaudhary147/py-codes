# 1243A
#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




#start the code from here

t=int(input())
for i in range(t):
	e=int(input())
	l=list(map(int,input().split()))
	ma=max(l)
	w=[0]*(ma+1)
	for i in l:
		w[i]+=1
	# print(w)
	for r in range(ma-1,-1,-1):
		w[r]+=w[r+1]
	# print(w)
	h=0
	for i in range(len(w)):
		if i>w[i]:
			h=i-1
			break
		if i==len(w)-1:
			h=i
	print(h)



