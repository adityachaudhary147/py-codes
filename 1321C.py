#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




#start the code from here
t=int(input())
st=input()
stlis=[]
for i in range(t):
	stlis.append(ord(st[i])-97)
# print(stlis)
stlis.append(-10)
for i in range(25,-1,-1):
	j=0
	while True:
		# print(j,stlis)
		if j>=(len(stlis)-1):
				break
			
		if stlis[j]==i:
			try:
				if j==0:
					if stlis[j]-1==stlis[j+1]:
						stlis.pop(0)
						# print(stlis,"man")
					else:
						j=j+1
				else:
					if stlis[j]-1==stlis[j-1] or stlis[j]-1==stlis[j+1]:
						stlis.pop(j)
						j=0
						# print(stlis,"woman")
					else:
						j=j+1
			except:
				break
			# print(stlis)
		else:
			j=j+1
print(t-len(stlis)+1)
