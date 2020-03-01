#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




#start the code from here

t=int(input())
for i in range(t):
	s=input()
	if s[-2:]=='po':
		print("FILIPINO")
		continue
	elif s[-4:]=='desu' or s[-4:]=='masu':
		print("JAPANESE")
		continue
	elif s[-5:]=="mnida":
		print("KOREAN")
		continue