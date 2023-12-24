## The Difference Between Copy and View

# The main difference between a copy and a view of an array is that the copy is a new array, 
# and the view is just a view of the original array.

# The copy owns the data and any changes made to the copy will not affect original array, 
# and any changes made to the original array will not affect the copy.

# The view does not own the data and any changes made to the view will affect the original array, 
# and any changes made to the original array will affect the view.

import numpy as np

# Copying the array

# Make a copy, change the original array, and display both arrays:

def copy1(array1):
    
    output1=np.array(array1)
    x=output1.copy()        # The copy SHOULD NOT be affected by the changes made to the original array.
    output1[0]=98
    print("\n ---Copying Array---")
    print("   The original array : ", output1)
    print("   The copied array : ", x)
    
array1=[1,2,3,4,5]
copy1(array1)

# Viewing the array

# Make a view, change the original array, and display both arrays:

def view1(array2):
    
    output2=np.array(array2)
    y=output2.view()        # The view SHOULD be affected by the changes made to the original array.
    output2[0]=89
    print("\n ---Viewing Array---")
    print("   The original array : ", output2)
    print("   The copied array : ", y)
    
array2=[1,2,3,4,5]
view1(array2)

# Make a view, change the view, and display both arrays:

def view2(array3):
    
    output3=np.array(array3)
    z=output3.view()
    z[-1]=99                # The original array SHOULD be affected by the changes made to the view.
    print("\n ---Changing View---")
    print("   The original array : ", output3)
    print("   The copied array : ", z)

array3=[1,2,3,4,5]
view2(array3)

# Checking if Array Owns its Data

# Every NumPy array has the attribute "base" that returns "None" if the array owns the data.
# Otherwise, the base  attribute refers to the original object.

def check1(array4):
    
    output4=np.array(array4)
    a=output4.copy()
    b=output4.view()
    print("\n ---Checking if Array Owns its Data---")
    print("   The check for copy : ", a.base)
    print("   The check for view : ", b.base)
    
array4=[1,2,3,4,5]
check1(array4)