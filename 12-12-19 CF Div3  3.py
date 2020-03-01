#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




# #start the code from here

# t=int(input())
# l=list(map(int,input().split()))
# e=[]
# for i in range(1,len(l)):
# 	if l[i-1]<l[i]:
# 		e.append(i)
# print(e)
# if len(e)==1:
# 	print(2)
# if len(e)==0:
# 	print(0)

# l=["a","b","c"]
# print("".join(l),end="")
t=int(input())
for i in range(int(t)):
    e=int(input())
    s=input()
    l=[]
    w=0
    for k in range(len(s)):
        
        if s[k]=="S":
            l.append("E")
        else:
            l.append("S")
    print("Case #",end="")
    print(i+1,end='')
    print(":","".join(l))