#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 


t=int(input())
dic=dict()
for i in range(t):
	a,b=map(str,(input().split()))
	if a in dic:
		dic[b]=dic[a]
		dic.pop(a)
	else:
		dic[b]=a
print(len(dic))
for i in dic:
	print(dic[i],i)