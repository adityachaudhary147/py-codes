#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 


t=int(input())
for q in range(t):
	n=int(input())
	a=list(map(int,input().split()))
	d={}
	for i in range(n):
		if a[i] not in d:
			d[a[i]]=[i]
		else:
			d[a[i]]+=[i]
	l=list(filter(lambda x:len(x)>=2,d.values()))
	l.sort(reverse=True)
	f=0
	for i in l:
		if i[-1]-i[0]>len(i)-1:
			print("YES")
			f=1
			break
	if f==0:
		print("NO")