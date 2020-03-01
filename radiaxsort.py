#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




#start the code from here


def countingsort(l,exp):
	if len(l)>0:
		ma=l[0]
	for i in range(len(l)):
		if ma<l[i]:
			ma=l[i]
	count=[0]*(ma+1)
	for i in range(len(l)):
		count[l[i]]+=1
	h=0
	print(count)
	t=0
	while t<ma+1:
		if count[t]>0:
			l[h]=t
			count[t]-=1
			h=h+1
		else:
			t=t+1

def radiaxsort(l):
	exp=1
	for i in range(len(l)):
		
