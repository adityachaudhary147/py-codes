#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 



# from collections import Counter
#start the code from here
t=int(input())
for i in range(t):
	n=int(input())
	l=list(map(int,input().split()))
	if n==1:
		print(l[0])
		continue
	else:
		# c=Counter(l)
		l.sort(reverse=True)
		print(*l)



