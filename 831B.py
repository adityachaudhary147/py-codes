# 831B.py
#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




#start the code from here


a=input()
b=input()
dic=dict()
for i in range(26):
	dic[a[i]]=b[i]
	dic[chr(ord(a[i])+65-97)]=chr(ord(b[i])+65-97)
for i in range(0,10):
	dic[str(i)]=str(i)
# print(dic)	
ans=[]
r=input()
for y in range(len(r)):
	ans.append(dic[r[y]])
print("".join(ans))	