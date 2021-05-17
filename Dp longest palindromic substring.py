#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




#start the code from here
st=input()
global ansarr
ansarr=[[-1 for i in range(len(st)+1)] for j in range(len(st)+1)]

def len_of_lps(instr,i,j):
	global ansarr
	if ansarr[i][j]!=-1:
		print("pre cal")
		return ansarr[i][j]

	if i==j:
		# print("equal")
		ansarr[i][j]=1
		return 1
	if instr[i]==instr[j]:
		# print("end equal")
		if i+1==j:
			ansarr[i][j]=2
			return 2
			# print("two")
		else:
			ansarr[i][j]=2+len_of_lps(instr,i+1,j-1)
			return 2+len_of_lps(instr,i+1,j-1)
	else:
		ansarr[i][j]=max(len_of_lps(instr,i+1,j),len_of_lps(instr,i,j-1))
		return max(len_of_lps(instr,i+1,j),len_of_lps(instr,i,j-1))
# NOT OPtimal way
for i in range(len(st)):
	for j in range(len(st)):
		if j>=i:
			h=0
			# print(i,j)
			# print(len_of_lps(st,i,j))
for l in range(2,len(st)+1):
	for i in range(len(st)-l+1):
		j=i+l-1
		print(i,j)
j=0

# master loop for i,j recursion in good time yess
print("alternative")
for i in range(1,len(st)+1):
	j=0
	while j+i<len(st):
		print(j,j+i)
		j=j+1
print(ansarr)
print(ansarr[0][8])
# print(len_of_lps(st,0,8))