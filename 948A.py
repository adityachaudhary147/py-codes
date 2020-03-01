#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




#start the code from here
n,m=map(int,input().split())
l=[]
for i in range(n):
	st=input()
	l1=[]
	for j in range(m):
		l1.append(st[j])
	l.append(l1)
# print(l)
h=0
for i in range(1,n-1):
	for j in range(1,m-1):
		# print(l[i][j],end="")
		if l[i][j]=='W':
			if l[i+1][j]=='S' or l[i][j+1]=='S' or l[i-1][j]=='S' or l[i][j-1]=='S':
				h=1
				break
		if l[i][j]=='S':
			if l[i+1][j]=='W' or l[i][j+1]=='W' or l[i-1][j]=='W' or l[i][j-1]=='W':
				h=1
				break
qw=[0,-1]
for i in qw:
	for j in range(m-1):
		if l[i][j]=='W':
			if l[i][j+1]=='S':
				h=1
		if l[i][j]=='S':
			if l[i][j+1]=='W':
				h=1
		


for j in qw:
	for i in range(n-1):
		if l[i][j]=='W':
			if l[i+1][j]=='S':
				h=1
		if l[i][j]=='S':
			if l[i+1][j]=='W':
				h=1


# print(l)
if h==1:
	print("NO")
else:
	print("YES")
	# print(l)

	for i in range(n):
		for j in range(m):
			if l[i][j]=='.':
				print("D",end="")
			else:
				print(l[i][j],end="")
		print()




