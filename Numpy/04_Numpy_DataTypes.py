## Data Types in NumPy

# i - integer
# b - boolean
# u - unsigned integer
# f - float
# c - complex float
# m - timedelta
# M - datetime
# O - object
# S - string
# U - unicode string
# V - fixed chunk of memory for other type ( void )

import numpy as np

# Getting the data type of an array object:

def dt1(array1):
    
    output1=np.array(array1)
    print("\n The data type of given array is : ", output1.dtype)
    
array1=[1,2,3,4,5]
dt1(array1)

# Getting the data type of an array containing strings:

def dt2(array2):
    
    output2=np.array(array2)
    print("\n The data type of given array is : ", output2.dtype)
    
array2=["hello","hai","welcome"]
dt2(array2)

# Creating Arrays With a Defined Data Type

# dtype that allows us to define the expected data type of the array elements

# Create an array with data type string:

def dt3(array3):
    
    output3=np.array(array3,dtype='S')   #creating arrays
    print("\n The array with data type as string : ", output3, "datatype", output3.dtype)
    
array3=[9,5,9,2,3,6]
dt3(array3)

# Converting Data Type on Existing Arrays

# The data type can be specified using a string, like 'f' for float, 'i' for integer etc.
# you can use the data type directly like float for float and int for integer.

# Change data type from float to integer by using 'i' as parameter value:

def dt4(array4):
    
    output4=np.array(array4)
    print("\n Changed data type from float to integer : ", output4.astype('i'))   #converting array
    
array4=[0.3,7.9,3.8,9.8]   
dt4(array4)

# Change data type from float to integer by using int as parameter value:

def dt5(array5):
    
    output5=np.array(array5)
    print("\n Changed data type from float to integer using 'i' : ", output5.astype(int))
    
array5=[0.654,9.123,4.876]   
dt5(array5)

# Change data type from integer to boolean:

def dt6(array6):
    
    output6=np.array(array6)
    print("\n Changed data type from integer to boolean using 'int' : ", output6.astype('bool'))
    
array6=[0,876,9,23454]   
dt6(array6)
    
