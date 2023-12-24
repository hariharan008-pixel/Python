## Reshaping arrays
## Reshaping means changing the shape of an array.
## By reshaping we can add or remove dimensions or change number of elements in each dimension.

import numpy as np

# Convert the following 1-D array with 12 elements into a 2-D array.
# The outermost dimension will have 4 arrays, each with 3 elements:

def reshaped(array1):
    
    result1=np.array(array1)
    print("The 4 arrays, each with 3 elements : ",  result1.reshape(4,3))
    
array1=[1,2,3,4,5,6,7,8,9,10,11,12]
reshaped(array1)

# Convert the following 1-D array with 12 elements into a 3-D array.
# The outermost dimension will have 2 arrays that contains 3 arrays, each with 2 elements:

def reshaped1(array2):
    
    result2=np.array(array2)
    print(" \n The 2 arrays that contains 3 arrays, each with 2 elements : ", result2.reshape(2,3,2))
    
array2=[12,11,10,9,8,7,6,5,4,3,2,1]
reshaped1(array2)

# Try converting 1D array with 8 elements to a 2D array with 4 elements in each dimension

def reshaped2(array3):
    
    result3=np.array(array3)
    print(" \n The 2D array with 4 elements : ", result3.reshape(2,4))

array3=[1,2,3,4,5,6,7,8]
reshaped2(array3)

# Unknown Dimension
# Meaning that you do not have to specify an exact number for one of the dimensions in the reshape method.
# Pass -1 as the value, and NumPy will calculate this number for you.

# Convert 1D array with 8 elements to 3D array with 2x2 elements

def reshaped3(array4):
    
    result4=np.array(array4)
    print("\n The 3D array with 2x2 elements using -1 : ", result4.reshape(2,2,-1)) 
    # We can not pass -1 to more than one dimension
    
array4=[88,44,9,2,90,11,14,55]
reshaped3(array4)

# Flattening the arrays
# Flattening array means converting a multidimensional array into a 1D array.
# We can use reshape(-1) to do this

# Convert the array into a 1D array

def reshaped4(array5):
    
    result5=np.array(array5)
    print("\n The Converted 1D array : ", result5.reshape(-1))
    
array5=[[1, 2, 3], [4, 5, 6]]
reshaped4(array5)
