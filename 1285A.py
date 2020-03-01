#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




#start the code from here
n=int(input())
s=(input())
w=s.count("L")
print(w+n-w+1)

