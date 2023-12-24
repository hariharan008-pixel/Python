# Joining Numpy Arrays
# Joining means putting contents of two or more arrays in a single array.

import numpy as np

# Joining two 1d arrays:

def joining1(array1,array2):
    
    result1=np.array(array1)
    result2=np.array(array2)
    print("\n The array after joining : ", np.concatenate((result1,result2)))
    
array1=[55,90,12,87]
array2=[87,34,80,23]
joining1(array1,array2)

# Joining two 2-D arrays along rows:

def joining2(array3,array4):
    
    result3=np.array(array3)
    result4=np.array(array4)
    print("\n The array after joining 2d array alog rows : ", np.concatenate((array3,array4),axis=1))
    
array3=[[9,8,7,6],[5,4,3,2]]
array4=[[11,22,33,44],[98,54,76,34]]
joining2(array3,array4)

# Joining Arrays Using Stack
# Stacking is same as concatenation, the only difference is that stacking is done along a new axis.
# If axis is not explicitly passed it is taken as 0.

def stack1(array5,array6):
    
    result5=np.array(array5)
    result6=np.array(array6)
    print("\n The array after stack : ", np.stack((result5,result6), axis=1))
    
array5=[1,2,3]
array6=[4,5,6]
stack1(array5,array6)

# Stacking Along Rows

def stack2(array7,array8):
    
    result7=np.array(array7)
    result8=np.array(array8)
    print("\n The array after stacking along rows : ", np.hstack((result7,result8)))
    
array7=[21,76,98]
array8=[87,32,99]
stack2(array7,array8)

# Stacking Along Columns

def stack3(array9,array10):
    
    result9=np.array(array9)
    result10=np.array(array10)
    print("\n The array after stacking along columns : ", np.vstack((result9,result10)))
    
array9=[8,3,8,9]
array10=[3,9,6,1]
stack3(array9,array10)

# Stacking Along Height (depth)

def stack4(array11,array12):
    
    result11=np.array(array11)
    result12=np.array(array12)
    print("\n The array after stacking along depth : ", np.dstack((result11,result12)))
    
array11=[234,765,987]
array12=[776,987,236]
stack4(array11,array12)

    