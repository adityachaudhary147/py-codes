#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




#start the code from here


t=int(input())
for i in range(t):
	a,b=map(int,input().split())
	s=input()
	l=list(map(int,input().split()))
	dic=dict()
	for j in range(a):
		dic[s[j]]=0
	arr=[0]*a
	for j in range(len(l)):
		arr[l[j]-1]+=1
	for k in range(len(arr)-2,-1,-1):
		arr[k]=arr[k]+arr[k+1]
	for k in range(len(arr)):
		arr[k]+=1
	# print(arr)
	for y in range(len(s)):
		dic[s[y]]+=arr[y]
	# print(dic)
	for e in range(26):
		if chr(97+e) in dic:
			print(dic[chr(97+e)],end=" ")
		else:
			print(0,end=" ")
	print()



