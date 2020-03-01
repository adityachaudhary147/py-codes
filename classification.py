#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 




#start the code from here


# from sklearn.datasets import load_iris
# iris=load_iris()
# print(type(iris))
# print(type(iris.data))
# print(type(iris.feature_names))
# print(iris.target_names)

# Import necessary modules
from sklearn import datasets
# import matplotlib.pyplot as plt

# Load the digits dataset: digits
digits =datasets.load_digits()

# # Print the keys and DESCR of the dataset
# print(digits.keys)
# print(digits.DESCR)

# # Print the shape of the images and data keys
# print(digits.images.shape)
# print(digits.data.shape)
from sklearn.neighbors import KNeighborsClassifier as KNN
from sklearn.model_selection import train_test_split 

# Create feature and target arrays
X =digits.data

y =digits.target

# Split into training and test set
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size =0.2, random_state=42, stratify=y)

# Create a k-NN classifier with 6 neighbors: knn
knn =KNN(n_neighbors=7)

# Fit the classifier to the data
knn.fit(X_train,y_train)

# Print the accuracy
print(knn.score(X_test,y_test),"Accuracy")
