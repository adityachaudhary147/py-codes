#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




#start the code from here
t=int(input())
for i in range(t):

	n=int(input())
	l1=list(map(int,input().split()))
	l2=list(map(int,input().split()))
	h=0
	q=set()
	for w in range(n):
		if l1[w]==l2[w]:
			h=0
			q.add(l1[w])
		else:
			c=l2[w]-l1[w]
			print(c,"or")
			if c<0:
				ch=-1
			if c>0:
				ch=1
			print(ch,"ch")
			if c in q or ch in q:
				h=0
				q.add(l2[w]-l1[w])
			else:
				print(c,"dik")
				h=1
	print(h)








