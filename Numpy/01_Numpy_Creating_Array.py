import numpy as np

# creating a numpy array using list:

def arr1(z):
    
    result1=np.array(z)
    print("\n Array from list : ", result1)
    print(" Type : ", type(result1))
    
z=[1,2,3,4]
arr1(z)

# creating a numpy array using tuple:

def arr2(x):
    
    result2=np.array(x)
    print("\n Array from tuple : ", result2)
    
x=(88,99,45,65,87)
arr2(x)

# 0-D Arrays
# Each value in an array is a 0-D array. Its a single element.

def arr3(x):
    
    result3=np.array(x)
    print("\n The 0D array : ", result3)
    
x=111
arr3(x)

# 1-D Arrays

def arr4(x):
    
    result4=np.array(x)
    print("\n The 1D array : ", result4)
    
x=[43,98,876]
arr4(x)

# 2-D Arrays

def arr5(a):
    
    result5=np.array(a)
    print("\n The 2D array : ", result5)
    
a=[[1, 2, 3], [4, 5, 6]]
arr5(a)

# 3-D Arrays
# Checking Number of Dimensions

def arr6(a):
    
    result6=np.array(a)
    print("\n The 3D array : ", result6)
    print(" The dimension of above array : ", result6.ndim)
    
a=[[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]]
arr6(a)

# Higher Dimensional Arrays

def arr7(y):
    
    result8=np.array(y,ndmin=5)
    print("\n The n-d array : ", result8)
    print(" The dimension of above n-d array : ", result8.ndim)
    
y=[7,9,2,7,4,6]
arr7(y)

