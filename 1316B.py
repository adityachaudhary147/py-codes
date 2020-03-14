#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




#start the code from here
t=int(input())
for i in range(t):
	n=int(input())
	st=input()
	w=sorted(st)
	print(w)
	for j in range(n):
		for k in range(n):
			if w[i]==st[j]:
				print(w[i])



