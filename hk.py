#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




#start the code from here

t=input()
e=["l","o","v","e"]
p=0
for i in range(len(t)):
	if t[i]==e[p]:
		p=p+1
		if p==3:
			break
if p>=3:
	print("I Love you, too!")
else:
	print("Let us breakup!")

