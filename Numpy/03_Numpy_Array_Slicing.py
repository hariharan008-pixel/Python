import numpy as np

## Slicing arrays
# Slicing in python means taking elements from one given index to another given index.
# We pass slice instead of index like this: [start:end].
# We can also define the step, like this: [start:end:step].

# Slicing elements from the beginning to index 4 (not included):

def slice1(array1):
    
    output1=np.array(array1)
    print("\n The sliced elements from the beginning to index 4 : ", output1[:4])
    
array1=[1,2,3,4,5,6,7]
slice1(array1)

# Negative Slicing

# Slice from the index 3 from the end to index 1 from the end:

def slice2(array2):
    
    output2=np.array(array2)
    print("\n The sliced elements from index 3 from end to index 1 : ", output2[-3:-1])
    
array2=[876,987,234,654,236,724,167,965]
slice2(array2)

# Slicing 1-D array

# Return every other element from index 1 to index 5:

def slice3(array3):
    
    output3=np.array(array3)
    print("\n The sliced elements from index 1 to index 5 stepping 2 : ", output3[1:5:2])
    
array3=[1, 2, 3, 4, 5, 6, 7]
slice3(array3)

# Slicing 2-D array

# From the second element, slice elements from index 1 to index 4 (not included):

def slice4(array4):
    
    output4=np.array(array4)
    print("\n The sliced elements from index 1 to index 4 in 2nd dim : ", output4[1,1:4])
    
array4=[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
slice4(array4)

# From both elements, slice index 1 to index 4 (not included), this will return a 2-D array

def slice5(array5):
    
    output5=np.array(array5)
    print("\n The sliced elements from index 1 to index 4 from both dim : ", output5[0:2,1:4])
    
array5=[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
slice5(array5)