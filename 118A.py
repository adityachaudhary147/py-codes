#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




#start the code from here

st=input()
l=[ord('a'),ord('A'),ord('e'),ord('E'),ord('i'),ord('I'),ord('o'),ord('O'),ord('U'),ord('u'),ord('y'),ord('Y')]
# print(l)
for i in range(len(st)):
	if ord(st[i]) in l:
		continue
	else:
		if ord(st[i])<97:
			print("."+chr(ord(st[i])+97-65),end="")
		else:
			print("."+st[i],end="")
