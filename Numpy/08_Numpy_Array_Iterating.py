## Iterating Arrays
## Iterating means going through elements one by one.

import numpy as np

# Iterating 1-D array

def iter1(array1):
    
    response1=np.array(array1)
    print("\n The 1D array after iteration : ")
    for i in response1:
        print(i)
        
array1=[54,98,23,87,96]
iter1(array1)

# Iterating 2-D array

def iter2(array2):
    
    response2=np.array(array2)
    print("\n The 2D array after iteration : ")
    for i in response2:
        print(i)

array2=[[1,2,3],[4,5,6]]
iter2(array2)
    
# Iterateing each element of the 2-D array:

def iter3(array3):
    
    response3=np.array(array3)
    print("\n The 2D array after iterating each element : ")
    for i in response3:
        for x in i:
            print(x)
            
array3=[[1,2,3],[4,5,6]]
iter3(array3)

# Iterating 3-D array

def iter4(array4):
    
    response4=np.array(array4)
    print("\n The 3D array after iteration : ")
    for i in response4:
        print(i)
    print(" The shape : ", response4.shape)
      
array4=[[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]]
iter4(array4)

# Iterateing each element of the 3-D array:

def iter5(array5):
    
    response5=np.array(array5)
    print("\n The 3D array after iterating each element : ")
    for i in response5:
        for a in i:
            for x in a:
                print(x)
                
array5=[[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]]
iter5(array5)

# Iterating Arrays Using nditer()
# By using nditer, we can iterate n dimensional arrays with ease

# Iterating 3-D array using nditer

def iter6(array6):
    
    response6=np.array(array6)
    print("\n The 3D array after iteration using nditer : ")
    for i in np.nditer(response6):
        print(i)
        
array6=[[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
iter6(array6)

# Iterating With Different Step Size

def iter7(array7):
    
    response7=np.array(array7)
    print("\n The step size of an array : ")
    for i in np.nditer(response7[::,::2]):
        print(i)
        
array7=[[1, 2, 3, 4], [5, 6, 7, 9]]
iter7(array7)

# Iterating Arrays Using ndenumerate()
# By using ndenumerate(), we can find the corresponding index of the element while iterating

# Enumerating 1D arrays elements 

def iter8(array8):
    
    response8=np.array(array8)
    print("\n The 1D array after enumeration : ")
    for x,y in np.ndenumerate(response8):
        print(x,y)
        
array8=[1, 2, 3]
iter8(array8)

# Enumerating 2D arrays elements

def iter9(array9):
    
    response9=np.array(array9)
    print("\n The 2D array after enumeration : ")
    for x,y in np.ndenumerate(response9):
        print(x,y)
        
array9=[[1, 2, 3, 4], [5, 6, 7, 8]]
iter9(array9)

# Enumerating 3D arrays elements

def iter10(array10):
    
    response10=np.array(array10)
    print("\n The 3D array after enumeration : ")
    for x,y in np.ndenumerate(response10):
        print(x,y)
        
array10=[[1, 2, 3, 4], [5, 6, 7, 8],[7,2,9,4]]
iter10(array10)

