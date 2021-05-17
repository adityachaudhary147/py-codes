#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




#start the code from here
t=int(input())
for i in range(t):
  n=int(input())

  print("Case #",end='')
  print(i+1,end="")
  print(":",end="")
  print()

  r=1
  print(1,1)
  n=n-1
  while n>0:
      r=r+1
      n=n-r+1
		
      if n<0:
          n=n+r-1
          r=r-1
          break
      if r==2:
          print(2,1)
      else:
          print(r,2)
		

  # print(n,r)
  while n!=0:
      print(r,1)
      n=n-1
      r=r+1




