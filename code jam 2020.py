#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 


n=5
l=[1,2,3,4,5]
a=set()
ftrace=[5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
for i in range(5):
	for j in range(5):
		for k in range(5):
			for l2 in range(5):
				for m in range(5):
					a.add(l[i]+l[j]+l[k]+l[l2]+l[m])
print(list(a))

	