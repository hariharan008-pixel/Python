import numpy as np

## Indexing in 1-D Array

# Getting third and fourth elements of an array and add them:

def ind1(array1):
    
    output1=np.array(array1)
    print("\n The addition of third and fourth element is : ", output1[2]+output1[3])
    
array1=[546,987,234,876,543,987]
ind1(array1)

## Indexing in 2-D Array

# Accessing the element on the 2nd row, 5th column:

def ind2(array2):
    
    output2=np.array(array2)
    print("\n The 2nd row 5th column is : ", output2[1,4])

array2=[[1,2,3,4,5], [6,7,8,9,10]]
ind2(array2)

## Indexing in 3-D Array

# Access the third element of the second array of the first array:

def ind3(array3):
    
    output3=np.array(array3)
    print("\n The third element of the second array of the first array : ", output3[0,1,2])
    
array3=[[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]]
ind3(array3)

## Negative Indexing

# Printing the last element from the 2nd dim:

def ind4(array4):
    
    output4=np.array(array4)
    print("\n The last element from the 2nd dim : ", output4[-1,-1])
    
array4=[[1,2,3,4,5], [6,7,8,9,10]]
ind4(array4)

