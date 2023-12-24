## Shape of an Array
## The shape of an array is the number of elements in each dimension.

import numpy as np

#Printing the shape of 2d array

def shape_of_an_array(array1):
    
    result=np.array(array1)
    print("The shape of array1 is : ", result.shape)

array1=[[5,8,7,6],[9,4,3,8],[1,7,3,6]]
shape_of_an_array(array1)

#Create an array with 5 dimensions using ndmin using a vector with values 1,2,3,4 

def array_with_5_dimension(array2):
    
    result1=np.array(array2, ndmin=5)
    print("\nThe 5 dim array2 is : ", result1) 
    print("The shape of array2 is : ", result1.shape)
    
array2=[88,99,44,66]
array_with_5_dimension(array2)