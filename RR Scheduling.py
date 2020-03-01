#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




#start the code from here


t=int(input()) 
# enter the number of process 
# enter the arrival time 
at=list(map(int,input().split()))
# enter bt
bt=list(map(int,input().split()))
btcopy=list(bt)
qt=2
readyq=[]
ct=[0]*t
wt=[0]*t
tat=[0]*t
time=0
i=0
pp=0
ntime=0
while True:
	if len(readyq)>1:
		pp=readyq[-1]+1
	while time<=at[pp] and at[pp]<=ntime and pp<t:
		readyq.append(pp)
		pp+=1
		print(0,at[pp],time,ntime,readyq)
	print()
	ntime=time
	if len(readyq)>0:
		pp=readyq.pop(0)
		print(readyq)
	else:
		break
	if btcopy[pp]>qt:
		btcopy[pp]-=2
		ntime=time+2
		readyq.append(pp)
	else:
		ct[pp]=ntime+btcopy[pp]
		btcopy[pp]=0
		wt[pp]=ct[pp]-bt[pp]
		tat[pp]=wt[pp]+bt[pp]


print(wt,tat,ct)





	




