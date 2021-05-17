#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 

# DP for length of longest commonsub sequence
#start the code from here
# input1
st1=input()
# input2
st2=input()

# recursion code
def lenlen(st1,st2,m,n):
	if m==0 or n==0 :
		print(0)
		return 0
	if st1[m-1]==st2[n-1]:
		print(m,n)
		return 1+lenlen(st1,st2,m-1,n-1)
	else:
		print(m,n)
		return max(lenlen(st1,st2,m-1,n),lenlen(st1,st2,m,n-1))
def help(st1,st2):
	# print(lenlen("AGGTAB","GXTXAYB",6,7))
	m=len(st1)

	n=len(st2)
	# using DP iterative version

	ans=[[0 for i in range(m+1)] for i in range(n+1)]
	for i in range(1,n+1):
		for j in range(1,m+1):
			if st2[i-1]==st1[j-1]:
				ans[i][j]=ans[i-1][j-1]+1

			else:
				ans[i][j]=max(ans[i-1][j],ans[i][j-1])
	reurn ans[n][m]

