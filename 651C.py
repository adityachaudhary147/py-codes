#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




#start the code from here
t=int(input())
l=[]
ans=0
adic=dict()
bdict=dict()
abdict=dict()
# print(abdict)
for i in range(t):
	a,b=map(int,input().split())
	h=0
	aac=0
	bbc=0
	abc=0
	if a in adic:
		ans+=adic[a]
		aac=1
	if b in bdict:
		ans+=bdict[b]
		bbc=1
	if (a,b) in abdict:
		abc=1
		ans-=abdict[(a,b)]
	if aac==1:
		adic[a]+=1
	else:
		adic[a]=1
	if bbc==1:
		bdict[b]+=1
	else:
		bdict[b]=1
	if abc==1:
		abdict[(a,b)]+=1
	else:
		abdict[(a,b)]=1
	
print(ans)


