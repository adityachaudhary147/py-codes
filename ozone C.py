#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




#start the code from here
a,b=map(int,input().split())
l=list(map(int,input().split()))
ans=1
if a>b:
	print(0)
	exit()
	# maine dondhliya h
	# reason doondlena jo bhi padh rha h 
	# mast h yaar
# l.sort() 
for i in range(a):
	for j in range(i+1,a):
		ans*=pow(abs(l[j]-l[i]),1,b)
		ans=pow(ans,1,b)
		if pow(ans,1,b)==0:
			print(0)
			exit()
print(pow(ans,1,b))
