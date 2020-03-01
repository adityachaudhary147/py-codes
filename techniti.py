#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




#start the code from here

l=list(map(str,input().split()))
n=int(l[0])

for i in range(1,int(l[0])+1):
	tw=l[i].count("2")
	th=l[i].count("3")
	fr=l[i].count("5")
	sv=l[i].count("7")
	if tw>=1:
		tw=1
	if th>=1:
		th=1
	if fr>=1:
		fr=1
	if sv>=1:
		sv=1
	u=[str(tw),str(th),str(fr),str(sv)]
	us=""
	us="".join(u)
	l[i]=int(us,2)
b,r=0,0
count1=0
print(l)
def findTriplets(arr, n):
	count=0
	for i in range(0 , n - 2):
		for j in range(i+1,n-1):
			for k in range(j + 1, n):
				if (arr[i]&arr[j]&arr[k]>0):
					count+=1
	return count
print(findTriplets(l[1:],len(l[1:])))






                


	
	
	
	