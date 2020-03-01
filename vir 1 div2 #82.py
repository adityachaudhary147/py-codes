#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




#start the code from here

trump=input()
fir,sec=map(str,input().split())
trlist=["S", "H", "D","C"]
rank=["6", "7", "8", "9", "T", "J", "Q", "K","A"]
if fir[1]==trump and sec[1]!=trump:
	print("YES")
elif fir[1]==sec[1]:
	if rank.index(fir[0])>rank.index(sec[0]):
		print("YES")
	else:
		print("NO")
else:
	print("NO")