#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 
# 3 7 9 11 21 27 33 49 63 77 81 99 121 147 189 231 243 297 343 363 441 539 567 693 729 847 891 1029 1089 1323 1331 1617 1701 2079 2187 2401 2541 2673 3087 3267 3773 3969 3993 4851 5103 5929 6237 6561 7203 7623
# [3, 7, 9, 11, 21, 27, 33, 49, 63, 77, 81, 99, 121, 147, 189, 231, 243, 297, 343, 363, 441, 539, 567, 693, 729, 847, 891, 1029, 1089, 1323, 1331, 1617, 1701, 2079, 2541, 2673, 3087, 3267, 3773, 3969, 4851, 5103, 6237, 7203, 7623, 8019, 9261, 11319, 11907, 14553, 15309]

def solve(A, B, C, D):
		ans=[]
		ansc=[]
		ansc.append(int(A))
		ansc.append(int(B))
		ansc.append(int(C))
		
		dic=dict()
		dic2=dict()
		dic2[A]=1
		dic2[B]=1
		dic2[C]=1
		k=0
		gh=0
		while k!=D:
			# print(ansc)
			a=min(ansc)
			
			if dic.get(a,0)==0:
				ans.append(a)
				ansc.remove(a)
				dic[a]=1
				ansc.append(int(a*a))
				dic2[a*a]=1
				s=len(ansc)
				# ansccp=set()
				for e in range(s):
					# print(dic2)
					# print(dic2.get(a*e,0))
					if dic2.get(a*ansc[e],0)==0:
						# print(ansc[e])
						ansc.append(int(a*ansc[e]))
						dic2[a*ansc[e]]=1
					# print()
				k=k+1
			else:
				nj=0

			# print(ansc)
		
		# ans=sorted(ans)
		
		return ans
print(solve(3,11,7,10))