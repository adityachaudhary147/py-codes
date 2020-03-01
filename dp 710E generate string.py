#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




#start the code from here
def genratestr(n,x,y):
	if n==1:
		return x
	else:
		return min(genratestr(n//2,x,y)+y+(n%2)*x,genratestr(n-1,x,y)+x)


n,x,y=map(int,input().split())
# print(genratestr(n,x,y))
dp=[0]*(n+1)
dp[1]=x
for i in range(2,n+1):
	dp[i]=min(dp[(i+1)//2]+y+(x if i&1 else 0),dp[i-1]+x)
print(dp[n])








