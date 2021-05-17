#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 
# subsequence vs substring
# class Solution:
# 	def __init__(self,st):
# 		self.s=st
# 	def longestPalindrome(self,s):
# 		st=[[s[i] for i in range(len(s))]for i in range(len(s))]
# 		print(st)
# 		for w in range(2,len(s)+1):
# 			# print(w)
# 			for i in range(len(s)-w+1):
# 				j=i+w-1
# 				h=0
# 				print(i,j)
# 				if s[i]==s[j] and w==2:
# 					st[i][j]=s[i]+s[j]
# 					h=1
# 				# print(w)
# 				if s[i]==s[j] and w!=2:
# 					# print("rt")
# 					st[i][j]=st[i][0]+st[i][j-1]+st[0][j]
# 				else:
# 					if h==0:
# 						a,b=st[i][j-1],st[i+1][j]
# 						if len(a)>len(b):
# 							st[i][j]=a
# 						else:
# 							st[i][j]=b
# 			print(st)
# 		return st[0][len(s)-1]
		
# a=Solution("ans")



def lps(str):
	n = len(str) 
	L = [[0 for x in range(n)] for x in range(n)] 
	for i in range(n): 
		L[i][i] = 1
 
	for cl in range(2, n+1): 
		for i in range(n-cl+1): 
			j = i+cl-1
			print(i,j)
			if str[i] == str[j] and cl == 2: 
				L[i][j] = 2
			elif str[i] == str[j]: 
				L[i][j] = L[i+1][j-1] + 2
			else: 
				L[i][j] = max(L[i][j-1], L[i+1][j]);
			print(L)
	return L[0][n-1]
class Solution:
	def __init__(self,st):
		self.s=st
	def longestPalindrome(self,s):
		st=[[1 for i in range(len(s))]for i in range(len(s))]
		start=0
		max_len=1
		for w in range(2,len(s)+1):
			# print(w)
			for i in range(len(s)-w+1):
				j=i+w-1
				h=0
				
				print(i,j)
				if s[i]==s[j] and w==2:
					print("a")
					st[i][j]=2
					start=i
					max_len=w
					h=1
				# print(w)

				if s[i]==s[j] and w!=2:
					print("b")
					if w%2==0:
						
						st[i][j]=+st[i][j-1]+2

					start=i
					max_len=w
				else:
					if h==0:
						if s[i]==s[j] and w%2==1:
							st[i][j]=st[i][j-1]+1
							start=i
							max_len=w
						print("c")
						a,b=st[i][j-1],st[i+1][j]
						if a>b:
							st[i][j]=a
						else:
							st[i][j]=b

						
		print(st)
		print(start,max_len)
		return s[start:start+max_len]
a=Solution("babadada")
print(a.longestPalindrome("babadada"))
