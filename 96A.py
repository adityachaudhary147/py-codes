#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




#start the code from here

st=input()
w=st[0]
cc=1
ma=1
for i in range(1,len(st)):
	if st[i]==w:
		cc+=1
	else:
		w=st[i]
		cc=1
	if cc>ma:
		ma=cc
	# print(cc)
if ma>=7:
	print("YES")
else:
	print("NO")

