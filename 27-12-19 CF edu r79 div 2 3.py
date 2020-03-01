#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




# #start the code from here

# # t=int(input())
# # for i in range(t):
# # 	n,m=
# # 	l=list(map(int,input().split()))
# # 	l2=list(map(int,input().split()))
# # 	l21=list(l2)
# # 	k=0
# # 	ans=0
# # 	for j in range(len(l)):
# # 		if l2[k]==l[j]:
# # 			ans+=2*k+1
# # 			k+=1
# # 		else:
# # 			if l[j] in l21:
# # 				ans+=1
# # 				l21.remove(l[j])
# # 	print(ans)




# t=int(input())
# for w in range(t):
# 	n,m=map(int,input().split())
# 	l=list(map(int,input().split()))
# 	l1=list(map(int,input().split()))
# 	sb=list(l1)
# 	k=0
# 	j=0
# 	ans=0
# 	i=0
# 	while i<n:
# 		if j<m :
# 			if l1[j] in sb:
# 				if l[i]==l1[j]:
# 					ans+=2*k+1
# 					j+=1
# 				else:
# 					if l[i] in sb:
# 						ans+=1
# 						sb.remove(l[i])
# 					k+=1
# 			else:
# 				j+=1
# 				i-=1
# 				k-=1
# 		else:
# 			break
# 		i+=1
# 	print(ans)



t=int(input())
for q in range(t):
	n,m=map(int,input().split())
	a=list(map(int,input().split()))
	b=list(map(int,input().split()))
	sb=set(b)
	k=0
	j=0
	ans=0
	c=0
	i=0
	while i<n:
		if j<m :
			if b[j] in sb:
				if a[i]==b[j]:
					ans+=2*k+1
					j+=1
				else:
					if a[i] in sb:
						ans+=1
						sb.remove(a[i])
					k+=1
			else:
				j+=1
				i-=1
				k-=1
		else:
			break
		i+=1
	print(ans)