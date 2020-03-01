#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




# start the code from here

from sklearn.datasets import fastfood
iris=load_fastfood()
print(type(iris))
print(type(iris.data))
print(type(iris.feature_names))
print(iris.target_names)
