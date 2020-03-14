#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




# Python 3 program To calculate 
# The Value Of nCr 


# def ncr(n, r, p): 
#     # initialize numerator 
#     # and denominator 
#     num = den = 1 
#     for i in range(r): 
#         num = (num * (n - i)) % p 
#         den = (den * (i + 1)) % p 
#     return (num * pow(den,  
#             p - 2, p)) % p 


 
def nCr(n, r): 
  
    return (fact(n) // (fact(r)  
                * fact(n - r))) 
  
# Returns factorial of n 
def fact(n): 
  
    res = 1
      
    for i in range(2, n+1): 
        res = res * i 
          
    return res 

#start the code from here
# t=int(input())
# for i in range(t):
a,b=map(int,input().split())
print(((nCr(b,a-1)*(a-2)*2)%998244353))

