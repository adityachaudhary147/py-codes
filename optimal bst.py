# optimal bst.py
#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




#start the code from here
n=3
keys = [10, 12, 20]  
freq = [34, 8, 50]

ans=[[0 for i in range(3)] for j in range(3)]

for w in range(3):
	ans[w][w]=freq[w]




for l in range(2,n+1):
	for i in range(n-l+1):
		j=i+l-1
		cost=float('inf')
		for r in range(i,j+1):
			



