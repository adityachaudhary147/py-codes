#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




#start the code from here

w,h=map(int,input().split())
w1,h1=map(int,input().split())
w2,h2=map(int,input().split())
for i in range(h,-1,-1):
	w=w+i
	if i==h1:
		w=w-w1
		if w<0:
			w=0
	elif i==h2:
		w=w-w2
		if w<0:
			w=0
print(w)




