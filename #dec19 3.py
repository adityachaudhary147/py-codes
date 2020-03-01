#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




#start the code from here

t=int(input())
for i in range(t):
	e=input()
	e1=input()
	wans=int(e)+int(e1)
	# print(wans)
	wans=str(wans)
	w=int(e,2)
	w1=int(e1,2)
	answe=1
	cc=1
	if int(e1,2)==0:
		print(0)
		continue
	k=0
	for j in range(len(wans)):
		if wans[k]=='1':
			cc+=1
			# print("cc1")
		if wans[k]=='0':
			cc=1
		if wans[k]=='2':
			cc+=1
			# print("cc2")
			if answe<=cc:
				answe=cc
				cc=1
				# print("cc3")
			cc=1
		k=k+1
	print(answe)
