#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




#start the code from here

n,mi=map(int,(input().split()))
ras=0
for i in range(100000):
	if n==mi:
		break
	if n>mi:
		ras=ras+1
		mi=mi+1
		continue
	elif mi%2:
		mi=mi+1
		ras=ras+1
		continue
	elif mi%2==0:
		mi=mi//2
		ras+=1
		continue
print(ras)





