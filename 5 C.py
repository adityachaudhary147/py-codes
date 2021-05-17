# 5 C
#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




#start the code from here
st=input()
st=list(st)
sorted_st=sorted(st)
# print(sorted_st,(set(st)))
dic=dict()
for i in range(26):
	dic[chr(ord('a')+i)]=0
for i in range(len(st)):
	dic[st[i]]+=1
listk=dic.values()
# print(listk)
# print(dic)
st1=[]
t=[]
u=[]
cc=0
w=0
while len(st)!=0:
	if sorted_st[0]==st[0]:
		re=st.pop(0)
		u.append(re)
		sorted_st.remove(re)

	elif len(t)>0 and sorted_st[w]==t[-1]:
		u.append(t.pop())
		w=w+1
		print("something")
	else:
		re=st.pop(0)
		t.append(re)
		sorted_st.remove(re)
t.reverse()
# print(u,t)
print("".join(u+t))